import os
from flask import Flask, jsonify, request
from flask_cors import CORS
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
    client = MongoClient(MONGO_URI)
except pymongo.errors.ConfigurationError:
    print("Invalid MongoDB URI. Check your .env settings.")
    sys.exit(1)

# Access the database and collection
db = client.theologylens
my_collection = db["verses"]

# Function to find all verses matching the given text
def find_verses(text):
    cursor = my_collection.find({"text": {"$regex": text, "$options": "i"}})  # case-insensitive match
    results = []

    for doc in cursor:
        results.append({
            "reference": f"{doc.get('book')} {doc.get('chapter')}:{doc.get('verse')}",
            "text": doc.get("text")
        })

    if results:
        return results
    else:
        return {"error": "No verses found"}, 404

# Flask app setup
app = Flask(__name__)
CORS(app)

@app.route('/verse', methods=['GET'])
def get_verses():
    text = request.args.get('text')
    if not text:
        return {"error": "Missing 'text' query parameter"}, 400
    return jsonify(find_verses(text))

if __name__ == '__main__':
    app.run(port=5000)