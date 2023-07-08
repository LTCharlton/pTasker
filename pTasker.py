#------------------
import sys
import SQL_Handler

#------------------global variables 

sql = SQL_Handler
user_input = sys.argv
connection = sql.Connect()

#-------------------functions

def addTask(task):
    new_task = task
    print("task added " + new_task)
    return 0

def showTasks():
    return 0

def removeTask():
    return 0

def commands():
    # this will show all available commands
    print("these are the commands you can use to alter your tasks:")
    print("add")
    print("delete")
    print("commands") 
    return 0

def readInput():
    if user_input[1].lower() == "add":
        addTask(user_input[2])
    elif user_input[1].lower() == "remove":
        removeTask()
    elif user_input[1].lower() == "commands":
        commands()
    return 0

def end():
    # apparently its good practice to close a database connection to free resources
    connection.close()
    return 0

#-------------------main
print(showTasks())
readInput()


end()