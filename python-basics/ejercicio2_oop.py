class Task:
    def __init__(self,task_id, title, description):
        self.id = task_id
        self.title = title
        self.description = description
        self.done = False

    def update(self, title=None, description=None, done=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if done is not None:
            self.done = done
    
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', description='{self.description}', done={self.done})"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list(self):
        return self.tasks

    def get(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update(self, task_id, title=None, description=None, done=None):
        for task in self.tasks:
            if task.id == task_id:
                task.update(title, description, done)
                return task
        return None

    def delete(self, task_id):
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