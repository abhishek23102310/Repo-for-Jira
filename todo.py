class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")

    def list_tasks(self):
        if self.tasks:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks found.")

def main():
    app = TodoApp()
    while True:
        print("\nTodo App Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task: ")
            app.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            app.remove_task(task)
        elif choice == '3':
            app.list_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
