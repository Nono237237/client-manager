import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("fr_FR")


cities = [
    "Yaounde", "Douala", "Bamenda", "Bafoussam", "Garoua",
    "Maroua", "Ngaoundere", "Bertoua", "Ebolowa", "Kumba",
    "Limbe", "Buea", "Kribi", "Nkongsamba", "Dschang", "Mutengene"

]

first_names = [
    "Nono", "Lukong", "Grace", "Emmanuel", "shannel",
    "Killian", "Linda", "Adel", "Desmond", "Mado",
    "Emba", "Ngong", "Lilian", "Blessing", "Tina",
    "Amina", "Fatima", "Celestine", "Rodrigue", "Pascal"
]

last_names = [
    "Ngelor", "Tchoumbou", "Nkwelle", "Fokam", "Mbianda",
    "Ngong", "Tabi", "Mbarga", "Kirk", "Mbah", "Motale"
    "Fon", "Nkeng", "Ndamukong", "Bello", "Nkwain",
    "Aluma", "Funkiun", "Nain", "Kelly", "Nkem"
]

conditions = [
    "Malaria", "Typhoid", "Hypertension", "Diabetes", "Asthma",
    "Respiratory Infection", "Anemia", "Skin Condition", "Skin Disease",
    "eye Infection", "Dental Issues", "General Checkup"
]

patients = []
for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    name = first + " " + last

    phone = "+237" + str(random.randint(10000000, 99999999))

    city = random.choice(cities)

    days_ago = random.randint(0, 365)
    date_joined = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")

    condition = random.choice(conditions)

    patients.append({
        "name": name,
        "phone": phone,
        "condition": condition,
        "location": city,
        "date_joined": date_joined
    })

file = open("data/patients.csv", "w", newline="")
writer = csv.DictWriter(file, fieldnames=["name", "phone", "condition", "location", "date_joined"])
writer.writeheader()
writer.writeheader()
writer.writerows(patients)
file.close()

print("Generated " + str(len(patients)) + " patients")
print("Saved to data/patients.csv")

