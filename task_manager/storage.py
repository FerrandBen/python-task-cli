import json

from .task import Task
import os

FILE_PATH = "data/tasks.json"

def save_tasks(task_list):

    data = [task.to_dict() for task in task_list]

    with open(FILE_PATH, "w") as file:
        json.dump(data, file)


def load_tasks():
    try:
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                data = json.load(file)
            return [Task.from_dict(item) for item in data]
    except json.JSONDecodeError:
        return []
