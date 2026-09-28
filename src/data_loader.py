import os
import pandas as pd
import requests
import re
from sqlalchemy import create_engine
from dotenv import load_dotenv

def clean_columns(df):
    """Converts column names to snake_case for easy handling."""
    def to_snake_case(column_name):
        column_name = re.sub(r"[^0-9a-zA-Z]+", "_", column_name).strip("_").lower()
        return re.sub(r"_+", "_", column_name)
    return df.rename(columns=to_snake_case).copy()

def load_from_csv(file_path):
    """Loads and cleans data from a CSV file."""
    df = pd.read_csv(file_path)
    return clean_columns(df)

def load_from_api(url):
    """Loads and cleans data from a JSON API endpoint."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    # Adjust this path based on the specific API's JSON structure
    df = pd.DataFrame(data.get("result", {}).get("records", []))
    return clean_columns(df)

def load_from_neon(table_name="ontario_housing"):
    """Loads and cleans data from the Neon PostgreSQL cloud database."""
    # 1. Load the hidden connection string from .env
    load_dotenv()
    neon_uri = os.getenv("NEON_DATABASE_URL")
    
    if not neon_uri:
        raise ValueError("NEON_DATABASE_URL is missing. Check your .env file.")
    
    # 2. Connect to the database and read the table
    engine = create_engine(neon_uri)
    df = pd.read_sql_table(table_name, engine)
    
    # 3. Return the cleaned dataframe
    return clean_columns(df)

# The block below only runs if you execute this file directly. 
# If you import these functions into another file, this block is safely ignored.
if __name__ == "__main__":
    print("Testing data_loader.py...")
    # Example local test
    # test_df = load_from_csv("../data/raw/ontario_housing.csv")
    # print(f"Loaded {test_df.shape[0]} rows.")