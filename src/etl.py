from __future__ import annotations

import pandas as pd


VALID_STATUSES = {"approved", "refunded", "failed"}


def clean_operational_data(df: pd.DataFrame) -> pd.DataFrame:
    curated = df.copy()
    curated["transaction_date"] = pd.to_datetime(curated["transaction_date"])
    curated["status"] = curated["status"].str.lower().str.strip()
    curated = curated[curated["status"].isin(VALID_STATUSES)]
    curated["amount"] = curated["amount"].clip(lower=0)
    curated["is_approved"] = (curated["status"] == "approved").astype(int)
    curated["is_refunded"] = (curated["status"] == "refunded").astype(int)
    curated["reporting_date"] = curated["transaction_date"].dt.date
    return curated.sort_values(["transaction_date", "transaction_id"]).reset_index(drop=True)


def build_kpi_summary(df: pd.DataFrame):
    total_transactions = len(df)
    total_revenue = float(df.loc[df["status"] == "approved", "amount"].sum())
    avg_order_value = float(df.loc[df["status"] == "approved", "amount"].mean())
    approval_rate = float(df["is_approved"].mean())
    refund_rate = float(df["is_refunded"].mean())

    kpi_df = pd.DataFrame(
        {
            "metric": [
                "total_transactions",
                "total_revenue",
                "average_order_value",
                "approval_rate",
                "refund_rate",
            ],
            "value": [
                total_transactions,
                round(total_revenue, 2),
                round(avg_order_value, 2),
                round(approval_rate, 4),
                round(refund_rate, 4),
            ],
        }
    )

    category_df = (
        df.groupby("product_category", as_index=False)
        .agg(transactions=("transaction_id", "count"), revenue=("amount", "sum"))
        .sort_values("revenue", ascending=False)
    )

    region_df = (
        df.groupby("region", as_index=False)
        .agg(transactions=("transaction_id", "count"), approved_rate=("is_approved", "mean"))
        .sort_values("transactions", ascending=False)
    )

    return kpi_df, category_df, region_df
