tasks = []
def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task {task} added to the list.")

def delete_task():
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
             tasks.pop(taskToDelete)
             print(f"Task {taskToDelete} has been removed")
        else:
             print(f"Task {taskToDelete} was not found")
             
    except:
        print("Invalid Input")
    

def view_tasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        for index, task in enumerate(tasks):
            print(f"Task #{index} {task}")


if __name__ == "__main__":
    print("Welcome to my To do list app")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("-------------------------------------------")
        print("1. Add new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")
        
        user_choice = int(input("Enter you choice: "))
       
        if(user_choice == 1):
             add_task()
        elif (user_choice == 2):
            delete_task()
        elif(user_choice == 3):
            view_tasks()
        elif(user_choice == 4):
            break
        else:
            print("Invalid input, please try again")
        
    print("Goodbye 💖💖")
            