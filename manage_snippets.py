# /scripts/manage_key_value_pairs.py
import pymongo

import sys


def insert_key_value(collection):
    key = input("Enter the key: ")
    print("Enter the value (multi-line code snippet). Press Enter twice to finish:")

    # Read multi-line input
    lines = []
    empty_lines = 0
    while True:
        line = input()
        if line == "":
            empty_lines += 1
            if empty_lines == 4:
                empty_lines=0
                break
        lines.append(line)
    value = "\n".join(lines)  # Combine lines into a single string

    if collection.find_one({"key": key}):
        print("Key already exists! Use the update option to modify it.")
    else:
        collection.insert_one({"key": key, "value": value})
        print("Key-value pair inserted successfully.")


def delete_key(collection):
    key = input("Enter the key to delete: ")
    result = collection.delete_one({"key": key})
    if result.deleted_count:
        print(f"Key '{key}' deleted successfully.")
    else:
        print(f"No key found with name: '{key}'.")

def view_all_keys(collection):
    print("Current key-value pairs:")
    for document in collection.find():
        print(f"Key: {document['key']}, Value: {document['value']}")

def update_value(collection):
    key = input("Enter the key to update: ")
    document = collection.find_one({"key": key})
    if document:
        new_value = input("Enter the new value: ")
        collection.update_one({"key": key}, {"$set": {"value": new_value}})
        print(f"Value for key '{key}' updated successfully.")
    else:
        print(f"No key found with name: '{key}'.")

def manage_key_value_pairs():
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["KeyValueDB"]
    collection = db["KeyValueCollection"]

    while True:
        print("\nKey-Value Pair Management")
        print("1. Insert Key-Value Pair")
        print("2. Delete Key")
        print("3. View All Key-Value Pairs")
        print("4. Update Value for Key")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            insert_key_value(collection)
        elif choice == "2":
            delete_key(collection)
        elif choice == "3":
            view_all_keys(collection)
        elif choice == "4":
            update_value(collection)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    manage_key_value_pairs()
