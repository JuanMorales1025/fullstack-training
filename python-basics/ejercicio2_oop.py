# Clase que representa una tarea individual
class Task:
    def __init__(self,task_id, title, description):
        # Identificador único de la tarea
        self.id = task_id
        # Título de la tarea
        self.title = title
        # Descripción de la tarea
        self.description = description
        # Estado de la tarea (por defecto, no está completada)
        self.done = False

    # Método para actualizar los valores de la tarea
    def update(self, title=None, description=None, done=None):
        # Si se envía un título nuevo, se actualiza
        if title is not None:
            self.title = title
        # Si se envía una descripción nueva, se actualiza
        if description is not None:
            self.description = description
        # Si se envía un valor para done, se actualiza
        if done is not None:
            self.done = done
    
    # Representación legible de la tarea (útil para depuración)
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', done={self.done})"
    

# Clase que administra un conjunto de tareas
class TaskManager:
    def __init__(self):
        # Lista donde se guardan las tareas
        self.tasks = []
        # Contador para asignar IDs automáticos
        self.next_id = 1

    # Crear una nueva tarea y agregarla al sistema
    def create(self, title, description):
        # Se crea la nueva tarea usando el siguiente ID disponible
        task = Task(self.next_id, title, description)
        # Se agrega la tarea a la lista
        self.tasks.append(task)
        # Se incrementa el ID para la próxima tarea
        self.next_id += 1
        return task

    # Método que devuelve la lista completa de tareas
    def list(self):
        return self.tasks

    # Buscar una tarea por su ID
    def get(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        # Si no se encuentra, retorna None
        return None
    
    # Actualizar una tarea buscando por ID
    def update(self, task_id, title=None, description=None, done=None):
        for task in self.tasks:
            if task.id == task_id:
                # Actualiza la tarea utilizando su propio método update
                task.update(title, description, done)
                return task
        return None

    # Eliminar una tarea por ID
    def delete(self, task_id):
        # Se genera una nueva lista sin la tarea cuyo id coincide
        self.tasks = [t for t in self.tasks if t.id != task_id]


if __name__ == "__main__":
    manager = TaskManager()

    print("=== Crear tareas ===")
    manager.create("Estudiar Vue", "Revisar Composition API")
    manager.create("Repasar Django", "Practicar modelos y vistas")
    print(manager.list())

    print("\n=== Actualizar tarea ===")
    manager.update(1, done=True)
    print(manager.get(1))

    print("\n=== Eliminar tarea ===")
    manager.delete(2)
    print(manager.list())