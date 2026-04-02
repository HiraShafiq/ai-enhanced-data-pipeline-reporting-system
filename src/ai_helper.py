"""Utilities and prompt templates for AI-assisted development workflows.

These helpers are intentionally simple so the repository can stay public and portable.
You can mention these in interviews as examples of how you use AI to improve speed and quality.
"""

SQL_REVIEW_PROMPT = """
Review the following SQL query for performance, readability, and correctness.
Suggest improvements for joins, filtering, aggregation logic, and naming consistency.
""".strip()

DEBUG_PROMPT = """
Analyze this Python ETL error and recommend the most likely root cause,
plus the safest code fix with minimal downstream impact.
""".strip()


def example_ai_workflow_notes() -> list[str]:
    return [
        "Use AI to review SQL queries before warehouse execution.",
        "Use AI to explain stack traces and propose targeted fixes.",
        "Use AI to generate test cases for ETL edge conditions.",
    ]
