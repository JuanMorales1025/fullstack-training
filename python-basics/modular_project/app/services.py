from .models import Task # Se importa la clase Task desde el módulo models

# Servicio encargado de manejar la lógica de negocio relacionada con las tareas
class TaskService:
    def __init__(self):
        # Lista donde se almacenan las tareas creadas
        self.tasks = []
        # Contador interno para asignar IDs automáticos a las tareas
        self.next_id = 1

    # Crear una nueva tarea y agregarla a la lista
    def create_task(self, title, description):
        # Se instancia un objeto Task con el ID actual
        task = Task(self.next_id, title, description)
        # Se almacena la tarea en la lista
        self.tasks.append(task)
        # Se incrementa el ID para la siguiente tarea
        self.next_id += 1
        return task

    # Devolver todas las tareas registradas
    def list_tasks(self):
        return self.tasks

    # Actualizar una tarea usando su ID y parámetros dinámicos (**kwargs)
    def update_task(self, task_id, **kwargs):
        # Busca la tarea por su ID
        task = self.get_task(task_id)
        # Si existe, actualiza sus atributos con los valores recibidos
        if task:
            task.update(**kwargs)
        return task

    # Eliminar una tarea filtrando la lista por ID
    def delete_task(self, task_id):
        # Se reconstruye la lista excluyendo la tarea con el ID dado
        self.tasks = [t for t in self.tasks if t.id != task_id]

    # Obtener una tarea específica por su ID
    def get_task(self, task_id):
        # Itera sobre las tareas para encontrar coincidencia
        for task in self.tasks:
            if task.id == task_id:
                return task
        # Si no existe, retorna None
        return None
