import sqlite3

def init_db():
    print("Starting init_db...")
    conn = sqlite3.connect("data/hospital.db")
    cursor = conn.cursor()

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS patients (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       phone TEXT,
       dob TEXT,
       condition TEXT,
       allergies TEXT,
       emergency_contact TEXT,
       location TEXT,
       priority TEXT,
       date_joined TEXT
       )
    """)
    print("CREATE TABLE executed")

    conn.commit()
    print("Committed")
    conn.close()
    print("Closed connection")

    if __name__ == "__main__":
     init_db()