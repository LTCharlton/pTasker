#------------------
import sys
import os
import sqlite3

#------------------global variables 
user_input = sys.argv
task = 0
db_file = "pTasker.db"

#-------------------functions

def readInput():
    return 0

def addTask():
    #this will save a task to a csv file within the folder
    return 0

def showTasks():
    return 0

def removeTask(task):
    return 0

#-------------------main
print(showTasks())

if not os.path.exists(db_file):
    # Create a new database file
    conn = sqlite3.connect(db_file)
    conn.close()
    print(f"New database file '{db_file}' created.")
else:
    print(f"Database file '{db_file}' already exists.")