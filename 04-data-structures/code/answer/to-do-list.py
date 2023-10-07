tasks = []

while True:
    # Display the menu options
    print("\nMenu:")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. View tasks")
    print("4. Exit")
    
    # Get user choice
    choice = input("Choose an option: ")
    
    # Add a task
    if choice == "1":
        # Get task name from user
        task_name = input("\nEnter task name: ")
        # Append a new task dictionary to the tasks list
        tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' added!")

    # Complete a task
    elif choice == "2":
        print("\nSelect a task to mark as complete:")
        # Display all tasks with a number for user to choose
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['task']}")
        # Get task number from user
        task_num = int(input("Task number: "))
        # Mark the selected task as completed
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as complete!")

    # View tasks
    elif choice == "3":
        print("\nTasks:")
        # Display all tasks with their completion status
        for task in tasks:
            status = "completed" if task["completed"] else "not completed"
            print(f"- {task['task']} ({status})")

    # Exit the program
    elif choice == "4":
        print("\nGoodbye!")
        break
    
    # Handle invalid choices
    else:
        print("\nInvalid choice. Please try again.")
