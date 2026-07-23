import os
from config import load_config
from clients import add_client, view_clients, search_by_name, search_by_business, count_clients, sort_clients

config = load_config()

owner = config.get("owner", "there")
first_name = owner.split()[0]
print("\n👋 Welcome back, " + first_name + "!")
print("📋" + config.get("app_name", "Client Manager") + " v" + config.get("version", "1.0"))

while True:
    try:
        print("\n=== Client Manager ===")
        print("1. Add New Client")
        print("2. View All Clients")
        print("3. Search Clients by name")
        print("4. Search Clients by Business Type")
        print("5. Client Statistics")
        print("6. Sort Clients")
        print("7. Exit")

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
            count_clients()
        elif choice == "6":
            sort_clients()
        elif choice == "7":
            print("Goodbye!")
            break

    except KeyboardInterrupt:
       print("\n\nGoodbye!")
       break
    except:
        print("Something unexpected happened. Restarting menu...")
        continue



