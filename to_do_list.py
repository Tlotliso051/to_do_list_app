# Procedural Programming (Funtions centric code)

print("TO DO LIST".center(50,"-"))
print()
print("What You Would Like To Do?\nTo Add Task or Delete Task?\ntype add to add-task or del to delete-task")
print()


def print_header(title):
    """
    Function to print a centered header.
    """
    print(title.center(50, "-"))


def list_of_option():
    """
    function displays the list of possible options.
    """
    print("1. Add\n2. Delete\n3. View tasks")


def add_or_delete_task():
    """
    Function to ask the user if they want to add or delete a task.
    Returns the user's choice.
    """
    
    while True:
        user_option = input("What do you want to do?: ").lower()
        if user_option in ["add", "delete", "view tasks"]:
            return user_option
        print("Please choose from the provided list of options.")


def get_task(user_task):
    """
    Function to get a task from the user.
    """
    return input(user_task)


def add_task(task_added):
    """
    Function to add a task to the list.
    """
    global list_of_tasks
    list_of_tasks.append(task_added)
    print("Task has been added successfully.")


def delete_task(task_deleted):
    """
    Function to delete a task from the list of tasks.
    """
    global list_of_tasks
    if task_deleted in list_of_tasks:
        list_of_tasks.remove(task_deleted)
        print("Task has been removed successfully.")
    else:
        print("Task not found in the list.")


def view_tasks():
    """
    Function to display the list of tasks.
    """
    global list_of_tasks
    print_header("LIST OF TASKS")
    if not list_of_tasks:
        print("No tasks available.")
    else:
        for count, item in enumerate(list_of_tasks, start=1):
            print(f"{count}. {item}")


def handle_commands():
    """
    Function to handle user commands for the to-do list.
    """
    list_of_option()
    while True:
        option = add_or_delete_task()
        if option == "add":
            add_task(get_task("Enter task: "))
        elif option == "delete":
            delete_task(get_task("Enter task: "))
        elif option == "view tasks":
            view_tasks()


if __name__ == "__main__":
    list_of_tasks = [] 
    handle_commands()
