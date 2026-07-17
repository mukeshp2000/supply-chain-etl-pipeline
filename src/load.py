from pathlib import Path
import logging

def load_data(customers, shipments, performance):
    output_folder = Path("data/processed")
    output_folder.mkdir(parents=True, exist_ok=True)

    customers.to_csv(
        output_folder / "customers_clean.csv",
        index=False
    )

    shipments.to_csv(
        output_folder / "shipments_clean.csv",
        index=False
    )

    performance.to_csv(
        output_folder / "performance_clean.csv",
        index=False
    )

    logging.info("Cleaned files saved to data/processed/")