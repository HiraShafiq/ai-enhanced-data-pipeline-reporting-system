import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    snowflake_account = os.getenv("SNOWFLAKE_ACCOUNT")
    snowflake_user = os.getenv("SNOWFLAKE_USER")
    snowflake_password = os.getenv("SNOWFLAKE_PASSWORD")
    snowflake_warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    snowflake_database = os.getenv("SNOWFLAKE_DATABASE")
    snowflake_schema = os.getenv("SNOWFLAKE_SCHEMA")
    snowflake_role = os.getenv("SNOWFLAKE_ROLE")

    @classmethod
    def snowflake_enabled(cls) -> bool:
        required = [
            cls.snowflake_account,
            cls.snowflake_user,
            cls.snowflake_password,
            cls.snowflake_warehouse,
            cls.snowflake_database,
            cls.snowflake_schema,
        ]
        return all(required)
