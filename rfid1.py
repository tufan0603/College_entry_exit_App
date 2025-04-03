"""
Author: Phalguni Banerjee
Version: 2.0
"""
import keyboard
from pymongo import MongoClient
import datetime
from flask import Flask, request, jsonify




app = Flask(__name__)
# Sample route
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# MongoDB Atlas Connection (Replace <username>, <password>, and <dbname>)
mongo_uri = "mongodb+srv://tufan:Tufan2023@entryddata.0rfkru0.mongodb.net/?retryWrites=true&w=majority&appName=entryDdata"

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client["CollegeData"]  # Replace with your database name
collection = db["entryExitData"]  # Replace with your collection name

def read_rfid():
    print("Listening for RFID input... Press 'q' to exit.")
    
    scanned_tag = ""  # Store the full tag
    while True:
        event = keyboard.read_event(suppress=True)
        
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == 'q':  # Exit on 'q' press
                print("Exiting...")
                break
            
            if key == 'enter':  # End of tag (RFID readers often send Enter after the tag)
                if scanned_tag:
                    print(f"RFID Tag: {scanned_tag}")

                    # Create document with given ID and timestamp
                    document = {
                        "RFID Tag":  scanned_tag,  # RFID TAG ID
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

                scanned_tag = ""  # Reset for next tag
            elif key.isalnum():  # Append alphanumeric characters
                scanned_tag += key

if __name__ == "__main__":
    read_rfid()
    app.run(host="0.0.0.0", port=8000)

# if __name__ == '__main__':
    
#   # Runs on http://127.0.0.1:5000