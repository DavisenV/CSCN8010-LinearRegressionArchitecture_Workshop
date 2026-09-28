import os
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Load the environment variables safely from the .env file
load_dotenv()

# 2. Retrieve the Neon connection string
neon_uri = os.getenv("NEON_DATABASE_URL")
if not neon_uri:
    raise ValueError("NEON_DATABASE_URL is missing. Check your .env file.")

# 3. Create the database connection engine
engine = create_engine(neon_uri)

# 4. Dynamically locate the processed data file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
csv_path = PROJECT_ROOT / "data" / "processed" / "ontario_housing_processed.csv"

print(f"Loading data from: {csv_path}")
df = pd.read_csv(csv_path)

# 5. Drop the 'id' column so it matches the Neon SQL schema
if 'id' in df.columns:
    df = df.drop(columns=['id'])

# 6. Push the data to the Neon database
print("Streaming to Neon...")
df.to_sql("ontario_housing", engine, if_exists="append", index=False)

print("Success! Data successfully streamed to Neon PostgreSQL.")