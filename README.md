# supply-chain-etl-pipeline
An automated supply chain ETL pipeline using Python, PostgreSQL, Apache Airflow and Docker.
## Technologies Used

- Python

- PostgreSQL

- Apache Airflow

- Docker

- Pandas

## Dataset

This project uses the Supply Chain Logistics Dataset.

Source:

https://www.kaggle.com/datasets/anirudhbadampudi/supply-chain-logistics-dataset

The raw dataset files are not included in this repository

Download the dataset and place the CSV files in:

`data/raw/`

## Airflow DAG Execution

The ETL pipeline is orchestrated with Apache Airflow and completed successfully.

![Airflow DAG Success](screenshots/airflow_dag_success.png)

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

  ## Airflow DAG Execution

The ETL pipeline is orchestrated using Apache Airflow and executes successfully through the DAG scheduler.

![Airflow DAG Success](screenshots/airflow_dag_success.png)

## Future Improvements

- Load cleaned data into PostgreSQL
- Containerize the pipeline with Docker
- Add automated testing with pytest
- Deploy Airflow using Docker Compose
