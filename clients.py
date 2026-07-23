#Handles all client operations

from config import load_config
config = load_config()

from datetime import datetime

from storage import load_clients, save_client

def clean_input(prompt, input_type="text"):
    while True:
        value = input(prompt).strip()
        
        if value == "":
            print("This field cannot be empty. Please try again.")
            continue
        if input_type == "text":
            return " ".join(value.split()).title()
        if input_type == "phone":
            value = value.replace("O", "0").replace("o", "0")
            if not value.isdigit():
                print("Phone number must contain digits only. Try again.")
                continue
            return value
        

def display_client(client):
    print("Name: " + client["name"])
    print("Phone: " + client["phone"])
    print("Business: " + client.get("business", "N/A"))
    print("Location: " + client.get("location", "N/A"))
    print("Date Joined: " + client.get("date_joined", "N/A"))
    print("---")


def add_client():
    clients = load_clients()
    max_clients = config.get("max_clients", 1000)
    if len(clients) >= max_clients:
        print("⚠️ Maximum number client limit of " + str(max_clients) + " reached." )
        return
    client = {}
    client["name"] = clean_input("Enter client's name: ", "text")
    client["phone"] = clean_input("Enter client's phone number: ", "phone")
    client["business"] = clean_input("Enter client's business type: ", "text")
    client["location"] = clean_input("Enter client's location: ", "text")
    client["date_joined"] = datetime.now().strftime(config.get("date_format", "%Y-%m-%d"))
    save_client(client)

def view_clients():
    clients = load_clients()
    if len(clients) == 0:
        print("No clients found.")
    else:
        print("\n--- All Clients ---")
        for client in clients:
            display_client(client)

def search_by_name():
    search = " ".join(input("Enter client name to search: ").strip().split()).lower()
    clients = load_clients()
    found = False
    for client in clients:
        if search in client["name"].lower():
            display_client(client)
            found = True
    if not found:
        print("No clients found with that name.")

def search_by_business():
    search = " ".join(input("Enter business type to search: ").strip().split()).lower()
    clients = load_clients()
    found = False
    for client in clients:
        if search in client.get("business", "").lower():
            display_client(client)
            found = True
    if not found:
        print("No clients found with that business type.")

def count_clients():
    clients = load_clients()
    total = len(clients)
    print("\n---Clients Statistics---")
    print("Total clients: " + str(total))

    business_types = {}
    for client in clients:
        business = client.get("business", "Unknown")
        if business in business_types:
            business_types[business] += 1
        else:
            business_types[business] = 1

    print("\nClients by Business Type:")
    for business, count in business_types.items():
        print(" " + business + ": " +str(count))


def sort_clients():
    clients = load_clients()
    if len(clients) == 0:
        print("No clients found.")
        return
    

    print("\nSort by:")
    print("1. Name")
    print("2. Business Type")
    print("3. Location")

    sort_choice = input("\nChoose sort option: ")

    if sort_choice == "1":
        sorted_clients = sorted(clients, key=lambda c: c["name"].lower())
        print("\n--- Clients Sorted by Name ---")
    elif sort_choice == "2":
        sorted_clients = sorted(clients, key=lambda c: c.get("business", "").lower())
        print("\n--- Clients Sorted by Business Type ---")
    elif sort_choice == "3":
        sorted_clients = sorted(clients, key=lambda c: c.get("location", "").lower())
        print("\n--- Clients Sorted by Location ---")
    else:
        print("Invalid option.")
        return
    
    for client in sorted_clients:
        display_client(client)
    
