import pandas as pd
from database import jobs_collection

# CHANGE PATH to your downloaded CSV
CSV_PATH = "data_job_posts.csv"

df = pd.read_csv(CSV_PATH)

# Convert NaN to None
df = df.where(pd.notnull(df), None)

jobs_collection.delete_many({})  # optional: clear old data
jobs_collection.insert_many(df.to_dict("records"))

print("Dataset successfully inserted into MongoDB")
