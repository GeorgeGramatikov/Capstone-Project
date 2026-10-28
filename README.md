# Northern Weather Analytics 🌨️

## Project Overview

Northern Weather Analytics is a data engineering project that analyzes historical weather patterns from 2000 to 2025 across seven cold-climate locations around the world. The project uses an ETL (Extract, Transform, Load) pipeline to process weather data and an interactive dashboard to explore temperature, snowfall, and rainfall trends.

The goal is to compare climates, identify seasonal patterns, and understand historical weather differences across some of the world's coldest regions.

## Locations

The project analyzes historical weather data from seven locations:

- Fairbanks, Alaska, USA
- Iqaluit, Nunavut, Canada
- McMurdo Station, Antarctica
- Nuuk, Greenland
- Oslo, Norway
- Reykjavík, Iceland
- Yakutsk, Russia

## Technologies Used

- **Python** — Data processing and ETL development
- **Pandas** — Data manipulation and transformation
- **PySpark** — Combining and cleaning weather datasets
- **SQL** — Querying, joining, and analyzing weather data
- **Snowflake** — Cloud data storage and analytics
- **Apache Airflow** — ETL workflow orchestration
- **Docker Compose** — Running the Airflow environment
- **Dash** — Building the interactive dashboard
- **Plotly** — Creating interactive charts and visualizations
- **Open-Meteo Historical Weather API** — Historical weather data source

## ETL Pipeline

The project follows an ETL workflow to transform raw weather data into an analytics-ready dataset.

1. **Extract:** Collect historical weather datasets from the Open-Meteo Historical Weather API for all seven locations.
2. **Transform:** Use Python, Pandas, and PySpark to combine datasets, check for cleaning records, and prepare the data for analysis.
3. **Validate:** Perform data quality checks to identify missing values, duplicates, and potential data issues.
4. **Load:** Store the processed weather data in Snowflake for querying and analysis.
5. **Orchestrate:** Use Apache Airflow to manage and execute the ETL workflow, with Docker Compose providing the containerized environment.
6. **Visualize:** Use Dash and Plotly to display historical weather patterns through an interactive dashboard.

## Interactive Dashboard

The dashboard allows users to filter weather data by location and year and explore historical climate trends.

### Dashboard Features

- **Temperature Analysis:** Explore average, minimum, and maximum temperatures across locations and years.
- **Snowfall Analysis:** Compare monthly and annual snowfall patterns.
- **Rainfall Analysis:** Examine monthly and total rainfall trends.
- **Location Filtering:** Select individual locations or compare multiple locations.
- **Year Filtering:** Analyze weather patterns across a selected historical period from 2000 to 2025.
- **Interactive Visualizations:** Explore weather trends through charts built with Plotly.

## Key Questions

The project helps answer questions such as:

- Which location has the lowest average temperature?
- Which locations experience the coldest and warmest conditions?
- How do average temperatures change throughout the year?
- Which locations receive the most snowfall?
- How does snowfall vary by month and location?
- Which locations experience the highest rainfall?
- How do seasonal precipitation patterns differ across locations?
- How have historical weather patterns changed between 2000 and 2025?
- What similarities and differences exist between the climates of these cold regions?

## Project Structure

```text
Northern-Weather-Analytics/
├── dags/                  # Airflow DAGs
├── scripts/               # Python ETL, loading, and dashboard scripts
├── sql/                   # SQL scripts for database setup and analysis
├── data/                  # Raw and processed weather datasets
├── .gitignore             # Files excluded from Git
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # Project documentation
```

## Getting Started

### Prerequisites

- Python
- Docker Desktop
- A Snowflake account with the required database permissions
- Git

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Northern-Weather-Analytics
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Configure Environment Variables

Create a local `.env` file with the Snowflake connection settings and other environment variables required by your project.

**Important:** Never commit your `.env` file or expose passwords, access tokens, or other credentials on GitHub.

### 3. Prepare the Data

Place the required historical weather CSV datasets in the local data directory expected by the ETL scripts.

The raw and processed datasets are excluded from Git to keep the repository lightweight. Make sure the required data files are available before running the pipeline.

### 4. Run the ETL Environment

Start the Airflow environment using Docker Compose:

```bash
docker compose up -d
```

Open the Airflow interface at:

http://localhost:8085

Enable and run the appropriate DAG to execute the ETL workflow. Ensure the required datasets, environment variables, and Snowflake configuration are available.

### 5. Launch the Dashboard

Install the project's dependencies in your configured Python environment. If your repository includes a `requirements.txt` file, run:

```bash
pip install -r requirements.txt
```

Start the dashboard:

```bash
python scripts/dashboard.py
```

Open the dashboard in your browser:

http://127.0.0.1:8050

The dashboard requires a successful Snowflake connection and the necessary weather tables to be populated.

## Data Storage

Processed weather records are stored in Snowflake, where SQL queries can filter locations, calculate summary statistics, and analyze historical temperature and precipitation patterns.

The dataset includes the following weather measurements:

- Mean temperature (°C)
- Maximum temperature (°C)
- Minimum temperature (°C)
- Precipitation (mm)
- Rainfall (mm)
- Snowfall (cm)

## Project Goals

- Develop an end-to-end data engineering pipeline.
- Practice ETL development using Python and PySpark.
- Automate data workflows using Apache Airflow.
- Store and analyze structured data in Snowflake.
- Apply data quality validation techniques.
- Build an interactive dashboard for exploring historical weather trends.

## Author

**George Gramatikov**

Data Engineering | Python | SQL | PySpark | Snowflake | Apache Airflow
