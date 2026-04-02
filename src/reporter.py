from __future__ import annotations

from pathlib import Path
import pandas as pd


OUTPUT_DIR = Path("data/output")


def export_outputs(
    curated_df: pd.DataFrame,
    kpi_df: pd.DataFrame,
    category_df: pd.DataFrame,
    region_df: pd.DataFrame,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    curated_df.to_csv(OUTPUT_DIR / "curated_transactions.csv", index=False)
    kpi_df.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)
    category_df.to_csv(OUTPUT_DIR / "category_summary.csv", index=False)
    region_df.to_csv(OUTPUT_DIR / "region_summary.csv", index=False)
