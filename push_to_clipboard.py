# /scripts/push_to_clipboard.py
import pymongo
import pyperclip
import sys

def push_to_clipboard():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["KeyValueDB"]
    collection = db["KeyValueCollection"]

    # User input
    key = input("Enter the key to fetch the value: ")

    # Fetch the value for the key
    document = collection.find_one({"key": key})
    if document:
        value = document["value"]
        pyperclip.copy(value)  # Copy to clipboard
        print(f"The value for key '{key}' has been copied to the clipboard.")
    else:
        print(f"No value found for key: '{key}'.")
    if key=="exit":
       sys.exit()
    else:
        push_to_clipboard()



if __name__ == "__main__":
    push_to_clipboard()
