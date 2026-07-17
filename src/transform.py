import pandas as pd


def transform_data(customers, shipments, performance):
    column = "customs_clearance_time_days"

    shipments[column] = pd.to_numeric(
        shipments[column],
        errors="coerce",
    )

    shipments[column] = shipments[column].fillna(
        shipments[column].median()
    )

    return customers, shipments, performance