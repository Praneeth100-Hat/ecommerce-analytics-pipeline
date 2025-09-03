# src/extract.py
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/online_retail.csv")   # your renamed file
STAGING_PATH = Path("data/staging_retail.csv")

def extract():
    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Missing {RAW_PATH}. Put your CSV inside the /data folder.")

    # Try safe encoding and skip bad lines
    df = pd.read_csv(RAW_PATH, encoding="latin-1", on_bad_lines="skip")

    print(f"✅ Columns detected: {list(df.columns)}")
    print(f"✅ Rows read: {len(df):,}")

    STAGING_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(STAGING_PATH, index=False)
    print(f"📦 Wrote staging file -> {STAGING_PATH.resolve()}")

if __name__ == "__main__":
    extract()
