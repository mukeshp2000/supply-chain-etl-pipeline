import logging
from pathlib import Path


def validate_data(customers, shipments, performance):
    rejected_folder = Path("data/rejected")
    rejected_folder.mkdir(parents=True, exist_ok=True)

    # Invalid customers: missing customer ID
    rejected_customers = customers[
        customers["customer_id"].isna()
    ].copy()

    valid_customers = customers[
        customers["customer_id"].notna()
    ].copy()

    # Invalid shipments: missing shipment ID or negative freight cost
    invalid_shipment_mask = (
        shipments["shipment_id"].isna()
        | (shipments["freight_cost"] < 0)
    )

    rejected_shipments = shipments[
        invalid_shipment_mask
    ].copy()

    valid_shipments = shipments[
        ~invalid_shipment_mask
    ].copy()

    # Invalid performance records
    invalid_performance_mask = (
        performance["shipments_processed"] < 0
    ) | (
        performance["warehouse_utilization_percent"] < 0
    ) | (
        performance["warehouse_utilization_percent"] > 100
    )

    rejected_performance = performance[
        invalid_performance_mask
    ].copy()

    valid_performance = performance[
        ~invalid_performance_mask
    ].copy()

    rejected_customers.to_csv(
        rejected_folder / "rejected_customers.csv",
        index=False
    )

    rejected_shipments.to_csv(
        rejected_folder / "rejected_shipments.csv",
        index=False
    )

    rejected_performance.to_csv(
        rejected_folder / "rejected_performance.csv",
        index=False
    )

    logging.info(
        "Rejected records saved: customers=%s, shipments=%s, performance=%s",
        len(rejected_customers),
        len(rejected_shipments),
        len(rejected_performance)
    )

    return valid_customers, valid_shipments, valid_performance