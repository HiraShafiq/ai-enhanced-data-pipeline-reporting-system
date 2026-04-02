# Architecture Overview

## Workflow
Raw operational data -> Python ETL -> Curated reporting tables -> Snowflake load -> SQL KPI transforms -> Reporting outputs

## Components
- `data_generator.py`: creates synthetic operational data for testing and demos
- `etl.py`: cleans, validates, transforms, and summarizes data
- `snowflake_loader.py`: optionally uploads curated datasets to Snowflake
- `reporter.py`: exports KPI outputs for dashboarding tools
- `ai_helper.py`: stores prompt templates and helper functions for AI-assisted SQL review and debugging

## Design Choices
- Modular code for clarity and reuse
- Environment-based Snowflake config for portability
- Synthetic data so the repository is safe to publish publicly
- Separate SQL folder for warehouse-side transforms
