from __future__ import annotations

import pandas as pd
from src.config import Settings


def load_to_snowflake_if_configured(df: pd.DataFrame, table_name: str) -> None:
    if not Settings.snowflake_enabled():
        print("Snowflake credentials not configured, skipping upload.")
        return

    try:
        import snowflake.connector
        from snowflake.connector.pandas_tools import write_pandas
    except ImportError:
        print("Snowflake connector not installed, skipping upload.")
        return

    conn = snowflake.connector.connect(
        account=Settings.snowflake_account,
        user=Settings.snowflake_user,
        password=Settings.snowflake_password,
        warehouse=Settings.snowflake_warehouse,
        database=Settings.snowflake_database,
        schema=Settings.snowflake_schema,
        role=Settings.snowflake_role,
    )

    try:
        success, nchunks, nrows, _ = write_pandas(conn, df, table_name, auto_create_table=True)
        print(f"Snowflake upload success={success}, chunks={nchunks}, rows={nrows}")
    finally:
        conn.close()
