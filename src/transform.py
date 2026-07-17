import pandas as pd


def transform_data(customers, shipments, performance):

    shipments["customs_clearance_time_days"] = pd.to_numeric(
        shipments["customs_clearance_time_days"],
        errors="coerce"
    )

    shipments["customs_clearnce_time_days"]=(
    shipments["customs_clearance_time_days"].fillna(
        shipments["customs_clearance_time_days"].median(),
        inplace=True
    )
    )
    return customers, shipments, performance