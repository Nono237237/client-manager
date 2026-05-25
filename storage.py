#Handles all file reading and writing for clients

def load_clients():
    clients = []
    try:
        file = open("clients.txt", "r")
        lines = file.readlines()
        file.close()

        client = {}
        for line in lines:
            line = line.strip()
            if line.startswith("Name:"):
                client["name"] = line[6:].strip()
            elif line.startswith("Phone:"):
                client["phone"] = line[7:].strip()
            elif line.startswith("Business:"):
                client["business"] = line[10:].strip()
            elif line.startswith("Location:"):
                client["location"] = line[10:].strip()
            elif line == "---":
              if client:
                clients.append(client)
                client = {}

    except:
        pass
    return clients


    
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




