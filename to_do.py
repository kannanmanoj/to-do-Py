import os

# File to store the tasks
TASKS_FILE = 'tasks.txt'

def display_menu():
    """Display the menu options."""
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task description: ")
    with open(TASKS_FILE, 'a') as file:
        file.write(task + '\n')
    print("Task added successfully!")

def view_tasks():
    """Display all tasks in the list."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
        if tasks:
            print("\nYour To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
        else:
            print("No tasks found.")
    else:
        print("No tasks file found.")

def remove_task():
    """Remove a task from the list."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
        if tasks:
            view_tasks()  # Display current tasks
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                with open(TASKS_FILE, 'w') as file:
                    file.writelines(tasks)
                print("Task removed successfully!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to remove.")
    else:
        print("No tasks file found.")

def main():
    """Main function to run the to-do list application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
