from src.data_generator import generate_sample_data
from src.etl import clean_operational_data, build_kpi_summary
from src.reporter import export_outputs
from src.snowflake_loader import load_to_snowflake_if_configured


def main() -> None:
    raw_df = generate_sample_data(rows=1500, seed=42)
    curated_df = clean_operational_data(raw_df)
    kpi_df, category_df, region_df = build_kpi_summary(curated_df)
    export_outputs(curated_df, kpi_df, category_df, region_df)
    load_to_snowflake_if_configured(curated_df, table_name="CURATED_TRANSACTIONS")
    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
