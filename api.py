import os
from flask import Flask, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import pymongo
import sys

# Load .env variables
load_dotenv()

# Get Mongo URI from environment
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
try:
    client = pymongo.MongoClient(MONGO_URI)
except pymongo.errors.ConfigurationError:
    print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
    sys.exit(1)

# Access the theologylens database and verses collection
db = client.theologylens
my_collection = db["verses"]

# Function to find a specific verse
def find_verse():
    my_doc = my_collection.find_one({"text": "In the beginning God created the heavens and the earth."})

    if my_doc:
        print("Found verse")
        verse = {
            "reference": f"{my_doc['book']} {my_doc['chapter']}:{my_doc['verse']}",
            "text": my_doc["text"]
        }
        print(verse)
        return verse
    else:
        print("No verse was found\n")
        return {"error": "Verse not found"}, 404

# Flask app setup
app = Flask(__name__)

@app.route('/verse', methods=['GET'])
def get_verse():
    return jsonify(find_verse())

if __name__ == '__main__':
    app.run(port=5000)
