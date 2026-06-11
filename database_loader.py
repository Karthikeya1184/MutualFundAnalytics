"""
Database Loader Module

Purpose:
Fetch mutual fund data and save it for processing.

Author:
Karthikeya Bammidi
"""
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

with engine.connect() as conn:

    tables = [
        "fact_nav",
        "fact_transactions",
        "fact_performance"
    ]

    for table in tables:

        count = conn.execute(
            text(
                f"SELECT COUNT(*) FROM {table}"
            )
        ).scalar()

        print(table, count)