from __future__ import annotations

import numpy as np
import pandas as pd


PRODUCTS = ["Payments", "Subscriptions", "Invoices", "Risk", "Billing"]
REGIONS = ["North America", "Europe", "Middle East", "Asia Pacific", "Latin America"]
STATUSES = ["approved", "approved", "approved", "refunded", "failed"]


def generate_sample_data(rows: int = 1000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2025-01-01", periods=90, freq="D")

    df = pd.DataFrame(
        {
            "transaction_id": [f"TXN-{i:05d}" for i in range(1, rows + 1)],
            "transaction_date": rng.choice(dates, rows),
            "customer_id": rng.integers(1000, 9999, rows),
            "product_category": rng.choice(PRODUCTS, rows),
            "region": rng.choice(REGIONS, rows),
            "status": rng.choice(STATUSES, rows),
            "amount": np.round(rng.uniform(10, 2500, rows), 2),
        }
    )
    return df
