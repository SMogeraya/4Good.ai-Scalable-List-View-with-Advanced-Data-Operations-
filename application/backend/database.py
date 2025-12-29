from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"

client = MongoClient(MONGO_URI)

db = client["job_dashboard"]
jobs_collection = db["jobs"]
