import keyboard
from pymongo import MongoClient
import datetime

mongo_uri = "mongodb+srv://tufan:Tufan2023@entryddata.0rfkru0.mongodb.net/?retryWrites=true&w=majority&appName=entryDdata"
#replce with your own mongo_uri

# Connect to MongoDB Atlas
client = MongoClient(mongo_uri)
db = client["CollegeData"]  # Replace with your database name
collection = db["entryExitData"]  # Replace with your collection name


def on_rfid_scan(event):
    if event.event_type == keyboard.KEY_DOWN:
        global rfid_buffer
        if event.name == 'enter':  # RFID scanner usually sends Enter after scanning
            print(f"RFID Tag Detected: {rfid_buffer}")
            

            # Create document with given ID and timestamp
            document = {  #MongoDB document structure
                        "RFID Tag": scanned_tag,  
                        "timestamp": datetime.datetime.now()  # Current timestamp
                    }
            # Insert into MongoDB Atlas
            try:
                insert_result = collection.insert_one(document)
                print(f"Inserted ID: {document['_id']}")
                print(f"Data: {document}")
            except Exception as e:
                print(f"Error inserting data: {e}")
                
            rfid_buffer = ''  # Reset buffer for next scan

        else:
            rfid_buffer += event.name

rfid_buffer = ''
keyboard.hook(on_rfid_scan)

print("Listening for RFID scans... Press 'ESC' to stop.")
keyboard.wait('esc')  # Keeps script running until ESC is pressed