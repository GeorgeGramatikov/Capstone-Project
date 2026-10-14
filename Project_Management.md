# WEATHER DATA ENGINEERING CAPSTONE PROJECT

## Task Timeline, Estimated Time Spent, and Completion Dates

### Project Overview

The goal of this project is to build a data engineering pipeline that processes historical weather data for cold-climate locations, including Antarctica, Iceland, Greenland, Norway, Yakutsk (Russia), Iqaluit (Canada), and Fairbanks (Alaska). The project uses Python, PySpark, Snowflake, SQL, Airflow, and Dash to clean, transform, store, analyze, and visualize weather data.

---

## EXPLORATORY DATA ANALYSIS (EDA) OF EACH DATASET

| | |
|---|---|
| **Estimated Time** | 3–4 hours |
| **Target Completion Date** | October 13, 2026 |
| **Tools** | CSV files, VS Code |
| **Status** | Completed |
| **Actual Time Spent** | 3 hours |
| **Actual Completion Date** | October 13, 2026 |

### Tasks

- Examine each weather CSV file.
- Identify the number of rows and columns in each dataset.
- Inspect column names, data types, and date ranges.
- Identify missing values, duplicate records, and unusual measurements.
- Compare the structure and quality of the datasets.
- Document initial findings and potential data-quality issues.

---

## IMPORTING DATA

| | |
|---|---|
| **Estimated Time** | 2–3 hours |
| **Target Completion Date** | October 13, 2026 |
| **Tools** | Python, PySpark, CSV files, Open-Meteo Historical Weather API |
| **Status** | Completed |
| **Actual Time Spent** | 2 hours |
| **Actual Completion Date** | October 13, 2026 |

### Tasks

- Obtain historical weather data from the Open-Meteo Historical Weather API.
- Save the retrieved data as CSV files.
- Import the seven weather datasets into PySpark.
- Confirm that each dataset contains the expected columns.
- Preserve location identifiers so the weather observations can be distinguished.
- Verify that the datasets cover the intended historical period.

---

## DATA CLEANING

| | |
|---|---|
| **Estimated Time** | 3–5 hours |
| **Target Completion Date** | October 15, 2026 |
| **Tools** | Python, PySpark, Pandas, VS Code |
| **Location** | Python script in VS Code; Airflow can schedule the cleaning workflow. |
| **Status** | Completed |
| **Actual Time Spent** | 5 hours |
| **Actual Completion Date** | October 14, 2026 |

### Tasks

- Read all seven weather CSV files into PySpark DataFrames.
- Inspect column names, inferred data types, and row counts using printSchema() and count().
- Combine all seven datasets into one DataFrame using unionByName().
- Check for missing and blank values across all columns.
- Count exact duplicate rows.
- Check for duplicate records based on location_id and date.
- Remove exact duplicate rows using dropDuplicates().
- Export the combined, deduplicated dataset to combined_weather.csv for Snowflake.

---

## DATABASE DESIGN (ERD AND DDL)

| | |
|---|---|
| **Estimated Time** | 2–3 hours |
| **Target Completion Date** | October 15, 2026 |
| **Tools** | SQL, Snowflake, Excalidraw, VS Code|
| **Status** | Completed |
| **Actual Time Spent** |  hours |
| **Actual Completion Date** | October , 2026 |

### Tasks

- Design the database schema for the weather project.
- Create an Entity-Relationship Diagram (ERD).
- Identify the tables, columns, primary keys, and foreign keys.
- Define appropriate data types for dates and weather measurements.
- Write the Data Definition Language (DDL) statements to create the tables.
- Create the database and schema in the selected database platform.
- Verify that the schema supports queries across locations and dates.

---

## OTHER DATA STORAGE

| | |
|---|---|
| **Estimated Time** | 1–2 hours |
| **Target Completion Date** | October 12, 2026 |
| **Tools** | Local file storage, CSV, Parquet, Snowflake |
| **Status** | Completed |
| **Actual Time Spent** | 1 hour |
| **Actual Completion Date** | October 12, 2026 |

### Tasks

- Store processed data in CSV or Parquet format where appropriate.
- Load the consolidated weather dataset into Snowflake.

---

## ETL PROCESS AND DOCUMENTATION

| | |
|---|---|
| **Estimated Time** | 4–6 hours |
| **Target Completion Date** | October 16, 2026 |
| **Tools** | Python, PySpark, Snowflake, SQL |
| **Status** | Completed |
| **Actual Time Spent** |  |
| **Actual Completion Date** |  |

### Tasks

#### Extract
- Read the seven weather CSV files.
- Load the data into PySpark DataFrames.
- Confirm that each file is accessible and contains the expected columns.

#### Transform
- Clean and standardize the data.
- Combine all seven datasets into one consolidated dataset.
- Preserve location identifiers.
- Validate dates, data types, missing values, and duplicate records.
- Ensure consistent measurement units.

#### Load
- Load the cleaned dataset into Snowflake.
- Confirm that the expected number of records was loaded.
- Query the final table to verify that the data is correct.

#### Documentation
- Explain each stage of the ETL process.
- Document the technologies and libraries used.
- Record data-cleaning rules and validation checks.
- Explain how the pipeline can be executed again.

---

## AIRFLOW DAGS

| | |
|---|---|
| **Estimated Time** | 3–5 hours |
| **Target Completion Date** | October 20, 2026 |
| **Tools** | Apache Airflow, Python, PySpark, Docker |
| **Status** | Planned |
| **Actual Time Spent** | __________ |
| **Actual Completion Date** | __________ |

### Tasks

- Create an Airflow Directed Acyclic Graph (DAG) to orchestrate the weather ETL pipeline.
- Define tasks for checking source files, running transformations, and validating or loading the output.
- Establish dependencies between the tasks.
- Configure retries and logging where appropriate.
- Run the DAG and verify that each task completes successfully.
- Troubleshoot failed tasks and dependency issues.
- Document the DAG structure and execution process.
- Capture screenshots or logs demonstrating successful execution.

---

## SNOWFLAKE (OPTIONAL / DATABASE COMPONENT)

| | |
|---|---|
| **Estimated Time** | 2–4 hours |
| **Target Completion Date** | October 21, 2026 |
| **Tools** | Snowflake SQL |
| **Status** | In Progress / Update |
| **Actual Time Spent** | __________ |
| **Actual Completion Date** | __________ |

### Tasks

- Create or verify the weather database and schema.
- Create the required tables and staging objects.
- Load the cleaned weather dataset.
- Validate the total number of records.
- Write SQL queries to calculate average monthly temperatures.
- Compare rainfall and snowfall across locations.
- Identify the coldest and warmest recorded temperatures.
- Verify that the data supports the dashboard's analytical questions.

---

## MACHINE LEARNING MODEL (OPTIONAL)

| | |
|---|---|
| **Estimated Time** | 4–6 hours |
| **Target Completion Date** | October 22, 2026 |
| **Tools** | Python, Pandas, Scikit-learn |
| **Status** | Optional |
| **Actual Time Spent** | __________ |
| **Actual Completion Date** | __________ |

### Tasks

- Select a suitable prediction problem, such as predicting daily mean temperature.
- Prepare the dataset and select relevant features.
- Split the data into training and testing sets using a time-aware approach.
- Train a baseline machine learning model.
- Evaluate the model using appropriate metrics, such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- Document the results and limitations.

---

## VISUALIZATION SKETCHES AND DASHBOARD PLANNING

| | |
|---|---|
| **Estimated Time** | 2–3 hours |
| **Target Completion Date** | October 22, 2026 |
| **Tools** | Paper sketches, diagrams, Plotly |
| **Status** | Planned |
| **Actual Time Spent** | __________ |
| **Actual Completion Date** | __________ |

### Tasks

- Sketch the proposed dashboard layout.
- Decide which charts best answer the project's research questions.
- Plan a line chart showing average monthly temperatures in Yakutsk.
- Plan comparisons of monthly rainfall and snowfall across locations.
- Plan charts showing the coldest and warmest recorded temperatures.
- Consider long-term temperature trends for Antarctica, where the data supports the analysis.
- Determine which filters and labels are needed.
- Document the purpose of each visualization.

---

## DASHBOARD CREATION

| | |
|---|---|
| **Estimated Time** | 5–7 hours |
| **Target Completion Date** | October 24, 2026 |
| **Tools** | Python, Dash, Plotly, Snowflake |
| **Status** | Planned |
| **Actual Time Spent** | __________ |
| **Actual Completion Date** | __________ |

### Tasks

- Build the interactive dashboard using Dash and Plotly.
- Connect the dashboard to the cleaned weather data or Snowflake queries.
- Create a line chart of average monthly temperatures in Yakutsk.
- Create charts comparing rainfall and snowfall across locations.
- Display the coldest and warmest recorded temperatures.
- Add charts showing average monthly temperatures by location.
- Include titles, axis labels, units, legends, and appropriate filters.
- Test the dashboard and verify that the charts display accurate results.
- Improve the layout and readability of the dashboard.

---

## PRESENTATION PREPARATION

| | |
|---|---|
| **Estimated Time** | 3–4 hours |
| **Target Completion Date** | October 26, 2026 |
| **Tools** | PowerPoint, project documentation, Dash dashboard |
| **Status** | Planned |
| **Actual Time Spent** | __________ |
| **Actual Completion Date** | __________ |

### Tasks

- Prepare slides introducing the project and its objectives.
- Explain the data sources and datasets.
- Present the database design and ERD.
- Explain the data-cleaning process and ETL pipeline.
- Describe how PySpark, Snowflake, and Airflow were used.
- Demonstrate the dashboard and discuss the key findings.
- Explain challenges, limitations, and possible future improvements.
- Practice the presentation and ensure it fits within the time limit.
- Prepare backup screenshots in case the live dashboard or database fails.
- Keep backup copies of the presentation and project files.

---

## ESTIMATED TOTAL PROJECT TIME

| Category | Estimated Time |
|----------|----------------|
| **Core project tasks** | Approximately 28–42 hours |
| **Optional machine learning** | Additional 4–6 hours |

> **Note:** Some tasks overlap because the same work contributes to multiple deliverables. Record actual hours as work progresses to avoid double-counting.

---

## PROJECT PRIORITIES

1. Complete exploratory data analysis and data importing.
2. Finish data cleaning and database design.
3. Complete and validate the ETL pipeline.
4. Load the consolidated data into Snowflake.
5. Build and test the Airflow DAG.
6. Sketch and build the dashboard visualizations.
7. Prepare and practice the final presentation.
8. Complete optional machine learning only if time permits.

---

## FINAL PROJECT CHECKLIST

- [ ] All source datasets inspected and documented.
- [ ] Weather data imported successfully.
- [ ] Data cleaning and validation completed.
- [ ] ERD and DDL completed.
- [ ] Raw and transformed data stored appropriately.
- [ ] ETL pipeline runs successfully.
- [ ] ETL documentation completed.
- [ ] Airflow DAG runs successfully.
- [ ] Snowflake tables and queries verified.
- [ ] Visualization sketches completed.
- [ ] Dashboard created and tested.
- [ ] Optional machine learning model completed, if selected.
- [ ] Presentation slides completed.
- [ ] Presentation practiced.
- [ ] Backup screenshots and project files prepared.

---

*END OF DOCUMENT*