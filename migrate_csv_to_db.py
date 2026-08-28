import csv
import sqlite3

def migrate():
    conn = sqlite3.connect("data/hospital.db")
    cursor = conn.cursor()

    with open("data/patients.csv", "r") as file:
        reader = csv.DictReader(file)
        count = 0
        for row in reader:
            cursor.execute("""
                INSERT INTO patients (name, phone, dob, condition, allergies, emergency_contact, location, priority, date_joined)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["name"], row["phone"], row["dob"], row["condition"],
                row["allergies"], row["emergency_contact"], row["location"],
                row["priority"], row["date_joined"]
            ))
            count += 1

    conn.commit()
    conn.close()
    print(f"Migrated {count} patients into the database.")

if __name__ == "__main__":
    migrate()