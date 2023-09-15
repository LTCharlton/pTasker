import sqlite3

DB_FILE = "../files/ptasker.db"


def save_to_file(usr_input):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    data = (usr_input,)

    test = cur.execute("INSERT INTO tasks (todo) VALUES (?)", data)
    print(test)
    conn.commit()
    conn.close()
    return None





