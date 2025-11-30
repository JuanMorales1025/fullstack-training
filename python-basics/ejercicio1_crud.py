tasks = [] #Inicializar una lista donde estaran las tareas almacenadas
next_id = 1 # Iterador con el que se podra asignar un id a cada tarea 
						# dentro de la lista

def create_task(title, description): # Funcion para crear una tarea
    global next_id # Se toma la variable next id
    task = {  # Las tareas seran de tipo diccionario 
        "id": next_id, 
        "title": title,
        "description": description,
        "done": False # Toda tarea se inicializa coomo "no hecha"
    }
    tasks.append(task) # Se agrega la tarea a la lista 
    next_id += 1 # Se suma uno mas  al id para la siguiente tarea
    return task # Se retorna la tarea que fue agregada a la lista (No es necesario) 

def list_tasks(): # Funcion para visualizar la lista de tareas completa
    return tasks # Retorna la lista

def update_task(task_id, title=None, description=None, done=None): # Funcion para editar una tarea 
    for task in tasks: # Se itera dentro la lista de tareas
        if task["id"] == task_id: # Comparativo para encontrar la tarea que se quiere editar
            if title is not None: # Comparativo para saber si queremos editar el titulo
                task["title"] = title # Se sustituye el titulo
            if description is not None: # Comparativo para saber si queremos editar la descripcion
                task["description"] = description # Se sustituye la descripcion
            if done is not None: # Comparativo para saber si queremos editar el estado de la tarea
                task["done"] = done # Se sustituye el estado de la tarea
            return task # Se retorna la tarea con los cambios hechos
    return None

def delete_task(task_id): #Funcion para borrar una tarea de la lista
    global tasks # Se llama a la lista de tareas
    tasks = [t for t in tasks if t["id"] != task_id] # Se sustituye la lista de tareas sin incluir la tarea que queremos eliminar
    

print(create_task("Sacar al perro", "Dar una vuelta"))
print(create_task("Hacer ejercicio", "Pierna hoy"))

print(list_tasks())

print(update_task(1, done=True))

delete_task(2)

print(list_tasks())

