from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import (
    functions as F,  #checking missing values and filtering duplicates
)

# create a spark session to process large datasets efficiently
spark = (
    SparkSession.builder
    .appName("WeatherDataETL")
    .master("local[*]") #run spark locally on my computer
    .getOrCreate()
)

# find the folder containing our weather csv files
data_folder = Path("data")

# The seven weather .csv files  
weather_files = [
    "Fairbanks_Alaska_Weather_Data.csv",
    "Iqaluit_Nunavut_Weather_Data.csv",
    "McMurdo_Station_Antarctica_Weather_Data.csv",
    "Nuuk_Greenland_Weather_Data.csv",
    "Oslo_Norway_Weather_Data.csv",
    "Reykjavik_Iceland_Weather_Data.csv",
    "Yakutsk_Russia_Weather_Data.csv"
]

# read each csv into a spark dataframe
weather_dataframes = []

#read all the .csv files -> save each to a DF -> save each DF to our spark list DF
for filename in weather_files: 
    file_path = (data_folder / filename).resolve()

    df = ( #read current .csv and create a DF for it
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(file_path))
    )

    #print out the DF and make sure it was read correctly including the types
    print(f"\nChecking {filename}")
    df.printSchema()
    print(f"Rows: {df.count()}")

    #save the current DF to our list DF weather_dataframes so store them all
    weather_dataframes.append(df)


combined_weather = weather_dataframes[0] #add the first dataframe

# combine all seven dataframes into one. Added the next 6 here.
for df in weather_dataframes[1:]:
    combined_weather = combined_weather.unionByName(df)

# The size of the combined dataset
print("\nCombined dataset:")
print(f"Rows: {combined_weather.count()}")
print(f"Columns: {len(combined_weather.columns)}")
combined_weather.printSchema()

# check for missing values in each column
print("\nMissing values by column:")

missing_checks = [
    F.sum(
        F.when(
            F.col(column).isNull()
            | F.trim(F.col(column).cast("string")).eqNullSafe(""),
            1
        ).otherwise(0)
    ).alias(column)
    for column in combined_weather.columns
]

combined_weather.select(*missing_checks).show(truncate=False)

# check for exact duplicate rows
print("\nExact duplicate rows:")
print(
    combined_weather.count()
    - combined_weather.dropDuplicates().count()
)

# check for duplicate dates within each location
print("\nDuplicate location/date records:")

if {"location_id", "date"}.issubset(set(combined_weather.columns)):
    duplicates = (
        combined_weather
        .groupBy("location_id", "date")
        .count()
        .filter(F.col("count") > 1)
    )

    duplicates.show(truncate=False)
else:
    print("Check the CSV column names for location_id and date.")

# remove only exact duplicate rows
combined_weather = combined_weather.dropDuplicates()

# save the combined data as one csv for snowflake
output_path = (data_folder / "combined_weather.csv").resolve()

# convert the spark dataframe to pandas and save it
combined_weather.toPandas().to_csv(
    output_path,
    index=False
)

print(f"\nCombined CSV saved to: {output_path}")
print(f"Final row count: {combined_weather.count()}")

# stop spark when finished
spark.stop()
