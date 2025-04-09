import json
import os

class Task:
    def __init__(self, task_id, title, description, category, status="Pendiente"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.status = status

    def mark_complete(self):
        self.status = "Completada"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f"[{self.task_id}] {self.title} ({self.category}) - {self.status}: {self.description}"


class TaskManager:
    _instance = None  # Patrón Singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename="tasks.json"):
        if not hasattr(self, 'initialized'):  # Para evitar reinit
            self.filename = filename
            self.tasks = self.load_tasks()
            self.initialized = True

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, task_id, new_title=None, new_description=None, new_category=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = new_title if new_title else task.title
                task.description = new_description if new_description else task.description
                task.category = new_category if new_category else task.category
                self.save_tasks()
                return True
        return False

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        self.save_tasks()

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def filter_tasks(self, by_category=None, by_status=None):
        filtered_tasks = self.tasks
        if by_category:
            filtered_tasks = [task for task in filtered_tasks if task.category == by_category]
        if by_status:
            filtered_tasks = [task for task in filtered_tasks if task.status == by_status]
        return filtered_tasks

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            data = json.load(f)
            return [Task.from_dict(t) for t in data]
