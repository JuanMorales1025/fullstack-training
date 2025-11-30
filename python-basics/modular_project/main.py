from app.services import TaskService # Se importa el servicio TaskService desde el módulo services

# Instancia del servicio que manejará toda la lógica de tareas
service = TaskService()

# Muestra el menú principal de la aplicación CLI
def show_menu():
    print("\n===== Task Manager CLI =====")
    print("1. Create task")
    print("2. List tasks")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")
    print("============================")

# Función para crear una nueva tarea pidiendo los datos al usuario
def create_task():
    title = input("Title: ")
    description = input("Description: ")
    # Se envía la información al servicio para crear la tarea
    task = service.create_task(title, description)
    print(f"Task created: {task}")

# Función para listar todas las tareas registradas
def list_tasks():
    tasks = service.list_tasks()
    # Si no hay tareas, notifica al usuario
    if not tasks:
        print("No tasks registered.")
        return
    # Imprime cada tarea existente
    for t in tasks:
        print(t)

# Función para actualizar una tarea
def update_task():
    # Solicita el ID de la tarea a modificar
    task_id = int(input("Task ID to update: "))

    # Campos opcionales para actualización
    title = input("New title (leave blank to skip): ")
    description = input("New description (leave blank to skip): ")
    done_input = input("Mark as done? (y/n/skip): ")

    # Manejo del campo opcional done
    done = None
    if done_input.lower() == "y":
        done = True
    elif done_input.lower() == "n":
        done = False

    # Llamada al servicio para actualizar la tarea
    task = service.update_task(
        task_id,
        title=title if title else None,
        description=description if description else None,
        done=done
    )

    # Se muestra el resultado al usuario
    if task:
        print("Updated:", task)
    else:
        print("Task not found.")

# Función para eliminar una tarea por ID
def delete_task():
    task_id = int(input("Task ID to delete: "))
    service.delete_task(task_id)
    print("Task deleted (if it existed).")

# Punto de entrada principal del programa
if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Select an option: ")

        # Controlador del menú según la opción ingresada
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
            # Entrada inválida del usuario
            print("Invalid option. Try again.")
