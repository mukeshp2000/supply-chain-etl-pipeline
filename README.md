# supply-chain-etl-pipeline
An automated supply chain ETL pipeline using Python, PostgreSQL, Apache Airflow and Docker.
[![ETL CI](https://github.com/mukeshp2000/supply-chain-etl-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/mukeshp2000/supply-chain-etl-pipeline/actions/workflows/ci.yml)

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core ETL pipeline development |
| Pandas | Data extraction, transformation, and validation |
| PostgreSQL | Storage for validated data |
| SQLAlchemy and psycopg2 | PostgreSQL connection and data loading |
| Apache Airflow | Workflow orchestration |
| Docker and Docker Compose | Containerized pipeline deployment |
| Pytest | Basic automated pipeline testing |
| GitHub Actions | Continuous integration and automated test execution |

## Dataset

This project uses the Supply Chain Logistics Dataset.

Source:

https://www.kaggle.com/datasets/anirudhbadampudi/supply-chain-logistics-dataset

The raw dataset files are not included in this repository

Download the dataset and place the CSV files in:

`data/raw/`

## Airflow DAG Execution

The ETL pipeline is orchestrated with Apache Airflow and completed successfully.

<img width="1512" height="982" alt="    airflow_dag_success" src="https://github.com/user-attachments/assets/fd5170ae-750d-473d-8686-bb7fb5aa3270" />


## Project Structure

```text
supply-chain-etl-pipeline/
│
├── dags/                  # Airflow DAG definitions
├── src/                   # ETL pipeline code
├── data/
│   ├── raw/               # Input datasets (ignored by Git)
│   ├── processed/         # Cleaned output files
│   └── rejected/          # Invalid records
├── logs/                  # Pipeline logs
├── notebooks/             # Exploratory analysis
├── screenshots/           # Project screenshots
├── requirements.txt
└── README.md
```

## ETL Workflow

Raw CSV Files
      ↓
Extract
      ↓
Validation
      ↓
Transformation
      ↓
Processed Files + Rejected Records
      ↓
Airflow Orchestration

## Features

- Automated ETL workflow
- Data validation checks
- Rejected records handling
- Airflow DAG orchestration
- Logging support
- Modular Python architecture
  
## Future Improvements

- Deploy the pipeline to a cloud platform such as AWS, Azure, or GCP
- Containerize Apache Airflow using Docker Compose
- Add incremental data loading
- Add pipeline failure alerts and monitoring
- Expand automated test coverage

 ## PostgreSQL Integration

The ETL pipeline writes validated data to cleaned CSV files and loads it into PostgreSQL using SQLAlchemy and psycopg2.

### PostgreSQL Tables

| Table | Rows |
|---|---:|
| customers | 750 |
| shipments | 728 |
| performance | 100 |

### Environment Configuration

Copy the example configuration:

```bash
cp .env.example .env
```

Then update `.env` with your local PostgreSQL credentials. The `.env` file is excluded from Git.

### Run the Pipeline

```bash
python src/pipeline.py
```

The pipeline performs:

```text
Raw CSV → Extract → Transform → Validate → Cleaned CSV + PostgreSQL
```

The same pipeline is orchestrated through the Apache Airflow DAG.

## Docker Deployment

The ETL pipeline and PostgreSQL database can run as isolated Docker services using Docker Compose.

### Services

- `etl`: Builds and runs the Python ETL pipeline
- `postgres`: Runs PostgreSQL 16 with persistent storage

### Run with Docker

Ensure the three source CSV files exist in `data/raw/`, then run:

```bash
docker compose up --build
```

The ETL container waits for PostgreSQL to become healthy, processes the source data, writes cleaned CSV files, and loads the three PostgreSQL tables.

### Verify the Database

```bash
docker compose exec postgres psql -U etl_user -d supply_chain_db -c "\dt"
```

### Stop the Containers

```bash
docker compose down
```

PostgreSQL data is retained in the Docker named volume.
