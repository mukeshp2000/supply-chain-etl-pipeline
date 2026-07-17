from extract import extract_data
from transform import transform_data
from validation import validate_data
from load import load_data
import logging

logging.basicConfig(
        filename="logs/etl.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


def run_pipeline():
    logging.info("pipeline started")

    customers, shipments, performance = extract_data()

    customers, shipments, performance = transform_data(
        customers,
        shipments,
        performance
    )
    customers, shipments, performance = validate_data(
        customers,
        shipments,
        performance
    )
    load_data(
        customers,
        shipments,
        performance
    )

    logging.info("Pipeline completed successfully!")
    print("pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
    
    

    