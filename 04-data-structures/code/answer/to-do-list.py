tasks = []

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. View tasks")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        task_name = input("\nEnter task name: ")
        tasks.append({"task": task_name, "completed": False})
        print(f"Task '{task_name}' added!")

    elif choice == "2":
        print("\nSelect a task to mark as complete:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task['task']}")
        task_num = int(input("Task number: "))
        tasks[task_num - 1]["completed"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as complete!")

    elif choice == "3":
        print("\nTasks:")
        for task in tasks:
            status = "completed" if task["completed"] else "not completed"
            print(f"- {task['task']} ({status})")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
