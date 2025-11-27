from .models import Task

class TaskService:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return self.tasks

    def update_task(self, task_id, **kwargs):
        task = self.get_task(task_id)
        if task:
            task.update(**kwargs)
        return task

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.id != task_id]

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
