#Handles menu and user interaction

from clients import add_client, view_clients, search_by_name, search_by_business

while True:
    try:
        print("\n=== Client Manager ===")
        print("1. Add New Client")
        print("2. View All Clients")
        print("3. Search Clients by name")
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



