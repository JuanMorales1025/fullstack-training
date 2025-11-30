# Clase que representa una tarea dentro del sistema
class Task:
    def __init__(self, task_id, title, description):
        # Identificador único de la tarea
        self.id = task_id

        # Título o nombre de la tarea
        self.title = title

        # Descripción detallada de la tarea
        self.description = description

        # Estado de la tarea (False = pendiente, True = completada)
        self.done = False

    # Método para actualizar los atributos de la tarea
    def update(self, title=None, description=None, done=None):
        # Actualiza el título si se envía un nuevo valor
        if title is not None:
            self.title = title
        
        # Actualiza la descripción si se envía un nuevo valor
        if description is not None:
            self.description = description
        
        # Actualiza el estado de completado si se envía un valor booleano
        if done is not None:
            self.done = done

    # Representación legible de la instancia (útil para depuración o impresión)
    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', done={self.done})"
