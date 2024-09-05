# models/task.py

class Task:
    def __init__(self, title, description=None):
        self.id = None  # ID will be assigned when the task is created
        self.title = title
        self.description = description

# In-memory storage for tasks
tasks = []
