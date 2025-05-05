import os
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime

# Load .env variables
load_dotenv()

# Get Mongo URI from environment
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["theologylens"]
collection = db["verses"]

# Load and clean CSV
df = pd.read_csv("web_reference.csv")
documents = []
for _, row in df.iterrows():
    doc = {
        "_id": int(row["Verse ID"]),
        "book": row["Book Name"],
        "book_number": int(row["Book Number"]),
        "chapter": int(row["Chapter"]),
        "verse": int(row["Verse"]),
        "text": str(row["Text"]),
        "reference": f"{row['Book Name']} {row['Chapter']}:{row['Verse']}",
        "themes": [],
        "embedding": [],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    documents.append(doc)

collection.insert_many(documents)
print(f"Inserted {len(documents)} verses.")
