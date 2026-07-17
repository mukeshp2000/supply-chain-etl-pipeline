from pathlib import Path
import logging
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def create_database_engine():
    load_dotenv()

    required_variables = [
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
    ]

    missing_variables = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing_variables:
        raise ValueError(
            f"Missing database variables: {', '.join(missing_variables)}"
        )

    database_url = URL.create(
        drivername="postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "5432")),
        database=os.getenv("DB_NAME"),
    )

    return create_engine(database_url)


def load_data(customers, shipments, performance):
    output_folder = Path("data/processed")
    output_folder.mkdir(parents=True, exist_ok=True)

    customers.to_csv(
        output_folder / "customers_clean.csv",
        index=False,
    )

    shipments.to_csv(
        output_folder / "shipments_clean.csv",
        index=False,
    )

    performance.to_csv(
        output_folder / "performance_clean.csv",
        index=False,
    )

    logging.info("Cleaned files saved to data/processed/")

    engine = create_database_engine()

    try:
        customers.to_sql(
            "customers",
            engine,
            if_exists="replace",
            index=False,
        )

        shipments.to_sql(
            "shipments",
            engine,
            if_exists="replace",
            index=False,
        )

        performance.to_sql(
            "performance",
            engine,
            if_exists="replace",
            index=False,
        )
    finally:
        engine.dispose()

    logging.info("Cleaned data loaded into PostgreSQL")