tasks = []

def show_tasks():
    print("\nYour Tasks:")
    if not tasks:
        print("No tasks added yet.")
        return

    for idx, t in enumerate(tasks, 1):
        print(f"{idx}. {t}")


def main():
    print("=== To-Do List Manager ===")

    while True:
        print("""
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter Task: ")
            tasks.append(task)
            print("Task Added!")

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            show_tasks()
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    print("Task Removed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
