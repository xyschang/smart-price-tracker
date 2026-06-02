import sqlite3
import os

DB_PATH = "data/prices.db"


def init_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS prices(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            url TEXT,
            target_price INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save(name, price):

    conn = sqlite3.connect(DB_PATH)

    conn.execute(
        "INSERT INTO prices(name,price) VALUES(?,?)",
        (name, price)
    )

    conn.commit()
    conn.close()


def get_all():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute("""
        SELECT name, price, time
        FROM prices
        ORDER BY id DESC
        LIMIT 20
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def get_history_by_name(name):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute("""
        SELECT name, price, time
        FROM prices
        WHERE name = ?
        ORDER BY id ASC
        LIMIT 30
    """, (name,))

    data = cursor.fetchall()
    conn.close()

    return data

def get_previous_price(name):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.execute("""
        SELECT price
        FROM prices
        WHERE name = ?
        ORDER BY id DESC
        LIMIT 2
    """, (name,))

    data = cursor.fetchall()

    conn.close()

    if len(data) >= 2:
        return data[1][0]

    return None