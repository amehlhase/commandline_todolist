tasks = []


def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list")


def listTasks():
    if not tasks:
        print("There are no tasks to do.")
    else:
        print("Current tasks: ")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # of the task to delete: "))
        if taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task #{taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")

    except:
        print("Invalid input.")


if __name__ == "__main__":
    ### Create a loop to run the aoo ###
    print("Welcome to your To-Do-List!")

    while True:
        print("\n")
        print("Please select one of the following options: ")
        print("---------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("What would you like to do? ")

        if (choice == "1"):
            addTask()

        elif (choice == "2"):
            deleteTask()

        elif (choice == "3"):
            listTasks()

        elif (choice == "4"):
            break

        else:
            print("Invalid input. Please try again! ")

    print("Goodbye!")
