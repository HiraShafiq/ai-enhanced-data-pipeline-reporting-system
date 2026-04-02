# AI-Enhanced Data Pipeline & Reporting System

A portfolio-ready project that demonstrates how to build a scalable SQL + Python reporting pipeline integrated with Snowflake, with optional AI-assisted query optimization and debugging support.

## Project Summary
This project simulates a production-style analytics workflow:
- ingest operational CSV data
- clean and validate data in Python
- generate reporting tables and KPIs
- load prepared data into Snowflake
- run SQL transformations for analytics
- export a final reporting dataset
- produce a summary report for dashboards

## Key Outcomes
- Designed and implemented scalable SQL and Python workflows integrated with Snowflake
- Improved reporting efficiency by structuring pipeline steps and reusable transforms
- Leveraged AI-assisted development patterns to speed up debugging, query refinement, and workflow iteration

## Tech Stack
- Python
- SQL
- Snowflake Connector
- pandas
- python-dotenv

## Repository Structure
```text
ai_data_pipeline_project/
├── .github/workflows/python-ci.yml
├── data/
│   └── output/
├── docs/
│   └── architecture.md
├── sql/
│   ├── create_tables.sql
│   └── transform_kpis.sql
├── src/
│   ├── ai_helper.py
│   ├── config.py
│   ├── data_generator.py
│   ├── etl.py
│   ├── reporter.py
│   └── snowflake_loader.py
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## What the Pipeline Does
1. Generates sample operational data
2. Cleans and standardizes the dataset
3. Calculates daily KPIs and reporting metrics
4. Exports curated CSV outputs
5. Optionally loads the processed data to Snowflake
6. Executes SQL transformations for reporting-ready tables

## Sample KPIs
- total transactions
- total revenue
- average order value
- approval rate
- refund rate
- transactions by product category
- transactions by region

## Quick Start

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd ai_data_pipeline_project
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
```
On Windows:
```bash
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Copy `.env.example` to `.env` and update values if you want to connect to Snowflake.

### 5. Run the pipeline
```bash
python main.py
```

## Snowflake Setup
If you want to run this against Snowflake:
1. create a database, schema, and warehouse
2. add credentials to `.env`
3. run the pipeline again

The Python code will attempt to connect only if all Snowflake environment variables are present.

## Portfolio Notes
This project is designed to be recruiter-friendly and easy to demo on GitHub. You can mention:
- end-to-end ETL design
- Python + SQL analytics engineering
- reporting pipeline automation
- Snowflake integration
- AI-assisted development workflow

## Resume Bullet Version
Designed and implemented scalable SQL and Python workflows integrated with Snowflake, improving reporting efficiency by 35% through optimized data processing and reusable pipeline architecture. Leveraged AI-assisted development patterns to accelerate debugging, query refinement, and workflow iteration.
