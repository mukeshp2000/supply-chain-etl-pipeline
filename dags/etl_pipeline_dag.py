from datetime import datetime
from pathlib import Path
import sys

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_FOLDER = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_FOLDER))

from pipeline import run_pipeline


with DAG(
    dag_id="supply_chain_etl_pipeline",
    description="Runs the supply-chain ETL pipeline",
    start_date=datetime(2026, 7, 17),
    schedule=None,
    catchup=False,
    tags=["etl", "supply-chain"],
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline,
    )