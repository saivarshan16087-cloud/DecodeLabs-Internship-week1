import json
import os
FILE_NAME = "tasks.json"
# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)
tasks = load_tasks()
# Add Task
def add_task():
    task = input("Enter a task: ")
    tasks.append({
        "task": task,
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully!")
# View Tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\n========== YOUR TASKS ==========")
    for i, task in enumerate(tasks, start=1):
        status = "✔ Completed" if task["completed"] else "❌ Pending"
        print(f"{i}. {task['task']} - {status}")
# Delete Task
def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        number = int(input("\nEnter task number to delete: "))
        if 1 <= number <= len(tasks):
            deleted = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted: {deleted['task']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
# Complete Task
def complete_task():
    view_tasks()
    if not tasks:
        return
    try:
        number = int(input("\nEnter completed task number: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
# Main Menu
def main():
    while True:
        print("\n===============================")
        print("        TO-DO LIST APP")
        print("===============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("\nThank you for using the To-Do List App.")
            break
        else:
            print("Invalid choice! Try again.")
# Start Program
if __name__ == "__main__":
    main()