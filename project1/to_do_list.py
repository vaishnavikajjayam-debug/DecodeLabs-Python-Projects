tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter your task: ")

        if task.strip():
            tasks.append(task)
            print("Task added successfully!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")