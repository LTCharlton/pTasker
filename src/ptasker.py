#------------------
import sys
import sql_handler

#------------------global variables 

sql = sql_handler
user_input = sys.argv

#-------------------main()


def main():
    read_input()
    return 0


#-------------------functions


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

def read_input():
    if len(user_input) > 1:
        if user_input[1].lower() == "add":
            add_task(user_input[2])
        elif user_input[1].lower() == "remove":
            remove_task()
    else:
        commands()
    return 0

#-------------------run

main()
