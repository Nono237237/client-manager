clients = [
    {"name": "John Doe", "business": "Plumbing"},
    {"name": "Mary", "business": "Welding"},
    {"name": "Grace", "business": "Hair Dresser"}

]

names_old = []
for c in clients:
    names_old.append(c["name"])
print("Old way:", names_old)

names = [c["name"] for c in clients]
print("Comprehension:", names)

plumbers = [c["name"] for c in clients if c["business"] == "Plumbing"]
print("Plumbers only:", plumbers)

long_names = [c["name"] for c in clients if len(c["name"]) > 4]
print("Long names only:", long_names)

def log_action(action, *args, **kwargs):
    print(f"Action: {action}")
    print(f"Extra positional info: {args}")
    print(f"Extra details: {kwargs}")

log_action("add_client", "priority", name="Paul Fru", business="Plumbing")