# src/load.py
import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

CLEAN_PATH = Path("data/cleaned_retail.csv")
DB_URL = "sqlite:///ecommerce.db"   # this will create ecommerce.db in project root

def load():
    if not CLEAN_PATH.exists():
        raise FileNotFoundError(f"Missing {CLEAN_PATH}. Run transform.py first.")

    # Load cleaned CSV
    df = pd.read_csv(CLEAN_PATH, encoding="latin-1")

    # Connect to SQLite
    engine = create_engine(DB_URL)

    # Write dataframe into SQLite
    df.to_sql("fact_sales", engine, if_exists="replace", index=False)

    # Add indexes for faster queries
    with engine.begin() as conn:
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_date ON fact_sales(InvoiceDate)"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_sales_customer ON fact_sales(CustomerID)"))

    print(f"✅ Loaded {len(df):,} rows into fact_sales table in ecommerce.db")

if __name__ == "__main__":
    load()
