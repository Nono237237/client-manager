import csv

old_clients = [
    {"name": "Munteh Shannel", "phone": "9480087478", "business": "Cleaning Service", "location": "N/A"},
    {"name": "John Doe", "phone": "0998434562", "business": "Plumbing", "location": "N/A"},
    {"name": "Mary", "phone": "09876543", "business": "Welding", "location": "N/A"},
    {"name": "Ngong Emmanuel", "phone": "650529383", "business": "Plumbing", "location": "N/A"},
]

file = open("clients.csv", "a", newline="")
writer = csv.DictWriter(file, fieldnames=["name", "phone", "business", "location"])
for client in old_clients:
    writer.writerow(client)
file.close()
print("Migration complete!")