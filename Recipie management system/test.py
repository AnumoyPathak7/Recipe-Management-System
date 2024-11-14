from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

# Set the database file path dynamically
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'RMS.db')

# Initialize the database and create the table if it doesn't exist
def init_db():
    print("entered into function")
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
    ''')
    conn.commit()
    conn.close()  # Close the connection after setting up the table
    print("table created")
    name="ANU"
    email="MOYY"
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    print(name,email)

if __name__ == '__main__':
    init_db()
