
tasks = []
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task added: {task}")

# Function to display all tasks
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['task']} [{status}]")

# Function to mark a task as completed
def mark_completed(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print(f"Task '{tasks[index]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

# Main menu loop
def main():
    print("== Simple To-Do List ==")
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            try:
                index = int(input("Enter task number to mark completed: ")) - 1
                mark_completed(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.")

# start
    main()
