tasks = []
next_id = 1

def create_task(title, description):
    global next_id
    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "done": False
    }
    tasks.append(task)
    next_id += 1
    return task

def list_tasks():
    return tasks

def update_task(task_id, title=None, description=None, done=None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if description is not None:
                task["description"] = description
            if done is not None:
                task["done"] = done
            return task
    return None

def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]

print(create_task("Sacar al perro", "Dar una vuelta"))
print(create_task("Hacer ejercicio", "Pierna hoy"))

print(list_tasks())

print(update_task(1, done=True))

delete_task(2)

print(list_tasks())

