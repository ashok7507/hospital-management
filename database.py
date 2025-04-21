import sqlite3

DB_NAME = 'hospital.db'

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS patients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        disease TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_patient(name, age, disease):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO patients (name, age, disease) VALUES (?, ?, ?)", (name, age, disease))
    conn.commit()
    conn.close()

def get_all_patients():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()
    conn.close()
    return data

def delete_patient(patient_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    conn.close()

