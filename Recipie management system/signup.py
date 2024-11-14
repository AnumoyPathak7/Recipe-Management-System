from flask import Flask, request, render_template
import sqlite3
import os
app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'RMS.db')


def init_db():
    with sqlite3.connect(DATABASE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS USERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                gender TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        conn.commit()
        conn.close()

@app.route('/')
def form():
    return render_template('signup.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['username']
    email = request.form['E-mail']
    gender = request.form['gender']
    password = request.form['pass']

  
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, gender, password) VALUES (?, ?, ?, ?)", (name, email, gender, password))
    conn.commit()
    conn.close()

    return f"Thank you, {name}. Your data has been saved!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
