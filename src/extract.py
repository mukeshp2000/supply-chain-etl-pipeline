import pandas as pd


def extract_data():
    customers = pd.read_csv("data/raw/customer.csv")
    shipments = pd.read_csv("data/raw/shipment.csv")
    performance = pd.read_csv("data/raw/logistics_performance.csv")

    return customers, shipments, performance