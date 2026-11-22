
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()

        if tasks:
            try:
                number = int(input("Enter task number to delete: "))

                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print("Deleted:", removed)
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye! Keep building.")
        break

    else:
        print("Invalid choice. Try again.")
