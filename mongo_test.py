from pymongo import MongoClient
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
# Sample route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# MongoDB Atlas Connection (Replace <username>, <password>, and <dbname>)
mongo_uri = "mongodb+srv://tufan:Tufan2023@entryddata.0rfkru0.mongodb.net/CollegeData"

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client["CollegeData"]  # Replace with your database name
collection = db["entryExitData"]  # Replace with your collection name

# Dynamic ID (can be from user input or another system)
generated_id = input("Enter the dynamically generated ID: ")  
generated_id = int(generated_id) if generated_id.isdigit() else generated_id  

# Create document with given ID and timestamp
document = {
    "RFID Tag":  generated_id,  # Use dynamically generated ID
    "createdAt": datetime.datetime.now(),  # Current timestamp
    "updatedAt": datetime.datetime.now()  # Current timestamp
}

# Insert into MongoDB Atlas
try:
    insert_result = collection.insert_one(document)
    print(f"Inserted ID: {document['_id']}")
    print(f"Data: {document}")
except Exception as e:
    print(f"Error inserting data: {e}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
  # Runs on http://127.0.0.1:5000
