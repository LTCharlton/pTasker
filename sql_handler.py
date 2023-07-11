import sqlite3

DB_FILE = "pTasker.db"


def save_to_file():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    query = "INSERT INTO table_name (name) VALUES "
    data = "56"
    cursor.execute(query, data)
    conn.commit()
    conn.close()
    return None





