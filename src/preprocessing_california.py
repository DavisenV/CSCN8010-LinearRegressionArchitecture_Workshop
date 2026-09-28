import pandas as pd
from pathlib import Path
import os

def main():
    # 1. Define paths
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    raw_path = PROJECT_ROOT / "data" / "raw" / "california_housing.csv"
    processed_dir = PROJECT_ROOT / "data" / "processed"
    processed_path = processed_dir / "california_housing_processed.csv"

    print(f"Loading raw California data from: {raw_path}")
    df = pd.read_csv(raw_path)

    # 2. Basic preprocessing (drop missing values)
    df_clean = df.dropna()

    # 3. Ensure the processed directory exists and save the file
    os.makedirs(processed_dir, exist_ok=True)
    df_clean.to_csv(processed_path, index=False)

    print(f"Success! Preprocessed California data saved to: {processed_path}")

if __name__ == "__main__":
    main()