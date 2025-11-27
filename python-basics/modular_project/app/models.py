class Task:
    def __init__(self, task_id, title, description):
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
        return f"Task(id={self.id}, title='{self.title}', done={self.done})"
    
    
