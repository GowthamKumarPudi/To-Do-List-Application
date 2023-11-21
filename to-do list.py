class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        print("\nTask List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.description} - Due Date: {task.due_date} - Priority: {task.priority} - Completed: {task.completed}")

    def mark_as_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Task '{self.tasks[task_index - 1].description}' marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
            print(f"Task '{task.description}' is updated.")
        else:
            print("Invalid Task Index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task.description}' is removed.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nOperations:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("0. Exit")

        choice = input("Enter your choice to perform an operation: ")

        if choice == "0":
            break
        elif choice == "1":
            description = input("Enter task description in detail: ")
            due_date = input("Enter due date of the task (optional): ")
            priority = input("Enter priority of the task (optional): ")
            new_task = Task(description, due_date, priority)
            todo_list.add_task(new_task)
        elif choice == "2":
            todo_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as completed: "))
            todo_list.mark_as_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to Update: "))
            new_description = input("Enter new description of task: ")
            new_due_date = input("Enter new due date of the task (optional): ")
            new_priority = input("Enter new priority of the task (optional): ")
            todo_list.update_task(task_index, new_description, new_due_date, new_priority)
        elif choice == "5":
            task_index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(task_index)
        else:
            print("Invalid choice. Please Try again....")

if __name__ == "__main__":
    main()
