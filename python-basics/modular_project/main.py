from app.services import TaskService

service = TaskService()

def show_menu():
    print("\n===== Task Manager CLI =====")
    print("1. Create task")
    print("2. List tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    print("============================")

def create_task():
    title = input("Title: ")
    description = input("Description: ")
    task = service.create_task(title, description)
    print(f"Task created: {task}")

def list_tasks():
    tasks = service.list_tasks()
    if not tasks:
        print("No tasks registered.")
        return
    for t in tasks:
        print(t)

def update_task():
    task_id = int(input("Task ID to update: "))
    title = input("New title (leave blank to skip): ")
    description = input("New description (leave blank to skip): ")
    done_input = input("Mark as done? (y/n/skip): ")

    done = None
    if done_input.lower() == "y":
        done = True
    elif done_input.lower() == "n":
        done = False

    task = service.update_task(task_id, 
                               title=title if title else None,
                               description=description if description else None,
                               done=done)
    if task:
        print("Updated:", task)
    else:
        print("Task not found.")

def delete_task():
    task_id = int(input("Task ID to delete: "))
    service.delete_task(task_id)
    print("Task deleted (if it existed).")

if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            create_task()
        elif option == "2":
            list_tasks()
        elif option == "3":
            update_task()
        elif option == "4":
            delete_task()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
