todo_list = []

def show_tasks():
    print("\n📋 To-Do List:")
    if not todo_list:
        print("Nothing to do!")
    for idx, task in enumerate(todo_list, start=1):
        print(f"{idx}. {task}")

def main():
    while True:
        print("\nOptions: [1] Add Task  [2] Remove Task  [3] View List  [4] Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.append(task)
            print("✅ Task added.")
        elif choice == '2':
            show_tasks()
            idx = int(input("Enter task number to remove: ")) - 1
            if 0 <= idx < len(todo_list):
                removed = todo_list.pop(idx)
                print(f"❌ Removed: {removed}")
            else:
                print("Invalid task number.")
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
