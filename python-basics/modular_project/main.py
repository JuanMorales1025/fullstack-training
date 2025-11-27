from app.services import TaskService

if __name__ == "__main__":
    service = TaskService()

    print("=== Crear tareas ===")
    service.create_task("Aprender Django", "Repasar conceptos fundamentales")
    service.create_task("Practicar Vue", "Hacer componentes con Composition API")
    print(service.list_tasks())

    print("\n=== Actualizar ===")
    service.update_task(1, done=True)
    print(service.get_task(1))

    print("\n=== Eliminar ===")
    service.delete_task(2)
    print(service.list_tasks())
