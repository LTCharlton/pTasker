import sqlite3

db_file = "pTasker.db"

def Connect():
   return sqlite3.connect(db_file)