import pandas as pd

from transform import transform_data


def test_transform_fills_invalid_and_missing_clearance_times():
    customers = pd.DataFrame(
        {"customer_id": [1, 2, 3]}
    )

    shipments = pd.DataFrame(
        {
            "customs_clearance_time_days": [
                "2",
                None,
                "invalid",
            ]
        }
    )

    performance = pd.DataFrame(
        {"metric": [1]}
    )

    _, transformed_shipments, _ = transform_data(
        customers,
        shipments,
        performance,
    )

    column = "customs_clearance_time_days"

    assert pd.api.types.is_numeric_dtype(
        transformed_shipments[column]
    )
    assert transformed_shipments[column].isna().sum() == 0
    assert transformed_shipments[column].tolist() == [
        2.0,
        2.0,
        2.0,
    ]