# src/transform.py
import pandas as pd
from pathlib import Path

STAGING_PATH = Path("data/staging_retail.csv")
CLEAN_PATH = Path("data/cleaned_retail.csv")

def transform():
    if not STAGING_PATH.exists():
        raise FileNotFoundError(f"Missing {STAGING_PATH}. Run extract.py first.")

    df = pd.read_csv(STAGING_PATH, encoding="latin-1")

    # Drop rows with missing values in important columns
    df = df.dropna(subset=["InvoiceNo", "StockCode", "Description", "Quantity", 
                           "InvoiceDate", "UnitPrice", "CustomerID", "Country"])

    # Remove duplicates
    df = df.drop_duplicates()

    # Convert InvoiceDate to datetime
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    # Filter out rows with non-positive quantities or prices
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Add a Revenue column
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]

    # Save cleaned dataset
    df.to_csv(CLEAN_PATH, index=False)
    print(f"✅ Cleaned rows: {len(df):,}")
    print(f"📦 Wrote cleaned file -> {CLEAN_PATH.resolve()}")

if __name__ == "__main__":
    transform()
