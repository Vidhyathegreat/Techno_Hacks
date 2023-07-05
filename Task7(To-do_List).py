class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed!")
        else:
            print("Task not found!")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print("- " + task)
        else:
            print("No tasks found.")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared!")


def main():
    todo_list = TodoList()
    while True:
        print("\n---- Todo List ----")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Clear All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            todo_list.clear_tasks()
        elif choice == "5":
            print("All The Best")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
