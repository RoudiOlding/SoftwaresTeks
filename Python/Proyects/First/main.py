from todo import load_tasks, add_task, view_tasks, remove_task

def main():
    tasks = load_tasks()

    print("WELCOME TO TODO APP")

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nEnter your choince: ")

        if choice == '1':
            task = input("Enter your task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            view_tasks(tasks)
            task_index = int(input("Enter the task index: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()