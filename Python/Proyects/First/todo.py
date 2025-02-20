TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: '{task}'")
    print("\n")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.")
        print("\n")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
            
        print("\n")

def remove_task(tasks, task_num):
    try:
        index = int(task_num) - 1
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task removed: '{removed}'")
        print("\n")
    except (ValueError, IndexError):
        print("⚠️ Invalid task number.")
        print("\n")