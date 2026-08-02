#Client Manager - Week 2
#Refactored with functions

def load_clients():
    clients = []
    try:
        file = open("clients.txt", "r")
        lines = file.readlines()
        file.close()

        client = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Name: "):
                client["name"] = line[6:]
            elif line.startswith("Phone:"):
                client["phone"] = line[7:]
            elif line.startswith("Business:"):
                client["business"] = line[10:]
            elif line.startswith("Location:"):
                client["location"] = line[10:]
            elif line == "---":
                if client:
                    clients.append(client)
                    client = {}
    except:
        pass
    return clients


def clean_input(prompt, input_type="text"):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("This field cannot be empty. Please try again.")
            continue

        if input_type == "text":
            return value.title()
        
        if input_type == "phone":
            value = value.replace("O", "0").replace("O", "0")
            if not value.isdigit():
                print("Phone number must contain digits only. Try again.")
                continue
            return value


def display_client(client):
    print("Name: " + client["name"])
    print("Phone: " + client["phone"])
    print("Business: " + client.get("business", "N/A"))
    print("Location: " + client.get("location", "N/A"))
    print("---")

def save_client(client):
    try:
        file = open("clients.txt", "a")
        file.write("Name: " + client["name"] + "\n")
        file.write("Phone: " + client["phone"] + "\n")
        file.write("Business: " + client["business"] + "\n")
        file.write("Location: " + client["location"] + "\n")
        file.write("---\n")
        file.close()
        print("✅ Client saved successfully.")
    except FileNotFoundError:
        print("Could not find the file. Please try again.")
    except PermissionError:
        print("Permission denied. Cannot write to file.")
    except:
        print("Something went wrong while saving. Please try again.")


def add_client():
    client = {}
    client["name"] = clean_input("Enter client's name: ", "text")
    client["phone"] = clean_input("Enter client's phone number: ", "phone")
    client["business"] = clean_input("Enter client's business type: ", "text")
    client["location"] = clean_input("Enter client's location: ", "text")
    save_client(client)

def view_clients():
    clients = load_clients()
    if len(clients) == 0:
        print("No clients found.")
    else:
        print("\n---All Clients---")
        for client in clients:
            display_client(client)

def search_by_name():
    search = input("Enter client name to search: ").lower()
    clients = load_clients()
    found = False
    for client in clients:
        if search in client["name"].lower():
            display_client(client)
            found = True
    if not found: 
        print("No client found with that name.")

def search_by_business():
    search = input("Enter business type to search: ").lower()
    clients = load_clients()
    found = False
    for client in clients:
        if search in client.get("business", "").lower():
            display_client(client)
            found = True
    if not found:
        print("No clients found with that business type.")

#Main menu
while True:
    try:
       print("\n=== Client Manager ===")
       print("1. Add New Client")
       print("2. View All Clients")
       print("3. Search Clients by Name")
       print("4. Search Clients by Business Type")
       print("5. Exit")

       choice = input("\nChoose an option: ")

       if choice == "1":
           add_client()
       elif choice == "2":
           view_clients()
       elif choice == "3":
           search_by_name()
       elif choice == "4":
           search_by_business()
       elif choice == "5":
           print("Goodbye!")
           break
       else:
           print("Invalid option. Please try again.")

    except KeyboardInterrupt:
        print("\n\nGoodbye!")
        break
    except:
        print("Something unexpected happened. Restarting menu...")
        continue   
           
       