#Handles all client operations

from storage import load_clients, save_client

def clean_input(prompt, input_type="text"):
    while True:
        value = input(prompt).strip()
        
        if value == "":
            print("This field cannot be empty. Please try again.")
            continue
        if input_type == "text":
            return "".join(value.split()).title
        if input_type == "phone":
            value = value.replace("O", "0").replace("o", "0")
            if not value.isdigit():
                print("Phone number must contain digits only. Try again.")
                continue
            return value
        

def display_client(client):
    print("Name: " + client["name"])
    print("Phone: " + client["phone"])
    print("Businesss: " + client.get("business", "N/A"))
    print("Location: " + client.get("location", "N/A"))
    print("---")


def add_client():
    client = {}
    client["name"] = clean_input("Enter client's name: ", "text")
    client["phone"] = clean_input("Enter client's phone number: ", "phone")
    client["business"] = clean_input("Enter client's business type: ", "text")
    client["location"] = clean_input("Enter clients location: ", "text")
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