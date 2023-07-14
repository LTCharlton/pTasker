#------------------
import sys
import sql_handler

#------------------global variables 

sql = sql_handler
user_input = sys.argv

#-------------------functions


def main():
    readnput()
    return 0


def add_task(task):
    new_task = task
    print("task added " + new_task)
    sql.save_to_file()
    return 0

def show_tasks():
    return 0

def remove_task():
    return 0

def commands():
    # this will show all available commands
    print("input command after script name:")
    print("add")
    print("delete")
    return 0

def readInput():
    if len(user_input) > 1:
        if user_input[1].lower() == "add":
            add_task(user_input[2])
        elif user_input[1].lower() == "remove":
            remove_task()
    else:
        commands()
    return 0

def end():
    # apparently its good practice to close a database connection to free resources
   
    return 0

#-------------------main
print(show_tasks())


end()

main()
