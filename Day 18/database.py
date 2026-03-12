import sqlite3
from datetime import datetime

def connect_db():
    conn = sqlite3.connect("pushups.db")
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pushups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        completed INTEGER,
        target INTEGER,
        date_time TEXT
    )
    """)

    conn.commit()
    conn.close()

from datetime import datetime

def save_progress(completed, target):
    conn = connect_db()
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO pushups (completed, target, date_time) VALUES (?, ?, ?)",
        (completed, target, now)
    )

    conn.commit()
    conn.close()

def load_progress():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT completed, target, date_time
    FROM pushups
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    return row

def load_last_progress():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT completed, target
    FROM pushups
    ORDER BY id DESC
    LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    return row

def show_history():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pushups")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()