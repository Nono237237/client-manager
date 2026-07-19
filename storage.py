#storage.py
#Handles all file reading and writing using csv

import csv
import os

#Auto-create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

FILENAME = "data/clients.csv"
HEADERS = ["name", "phone", "business", "location"]

def load_clients():
    clients = []
    try:
        if not os.path.exists(FILENAME):
            return clients
        file = open(FILENAME, "r", newline="")
        reader = csv.DictReader(file)
        for row in reader:
            clients.append(dict(row))
        file.close()
    except Exception as e:
        print("Error loading clients:", e)
    return clients

def save_client(client):
    try:
        file_exists = os.path.exists(FILENAME)
        file = open(FILENAME, "a", newline="")
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(client)
        file.close()
        print("Client saved successfully.")
    except Exception as e:
        print("Error saving client:", e)