<<<<<<< HEAD

import sqlite3

DB_NAME = 'url_data.db'

#  Create the database and table
def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            label TEXT,
            length INTEGER,
            dots INTEGER,
            hyphens INTEGER,
            digits INTEGER,
            at_symbol INTEGER,
            prediction TEXT
        )
    ''')
    conn.commit()
    conn.close()

#  Function to insert a URL and its features
def insert_url(data):
    """
    data: tuple(url, label, length, dots, hyphens, digits, at_symbol, prediction)
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO urls (url, label, length, dots, hyphens, digits, at_symbol, prediction)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

# Only create the database when running this file directly
if __name__ == "__main__":
    create_db()
=======

import sqlite3

DB_NAME = 'url_data.db'

#  Create the database and table
def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            label TEXT,
            length INTEGER,
            dots INTEGER,
            hyphens INTEGER,
            digits INTEGER,
            at_symbol INTEGER,
            prediction TEXT
        )
    ''')
    conn.commit()
    conn.close()

#  Function to insert a URL and its features
def insert_url(data):
    """
    data: tuple(url, label, length, dots, hyphens, digits, at_symbol, prediction)
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO urls (url, label, length, dots, hyphens, digits, at_symbol, prediction)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', data)
    conn.commit()
    conn.close()

# Only create the database when running this file directly
if __name__ == "__main__":
    create_db()
>>>>>>> 6be99264d218af05c6ed951ba699d97a6e295199
    print("Database created successfully!")