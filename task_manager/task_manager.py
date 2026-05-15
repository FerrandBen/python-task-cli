from task import Task


class Task_manager:

    def __init__(self):
        self.task_list: list = []

    def add_task(self, title):

        newTask = Task(title)

        self.task_list.append(newTask)

        return newTask

    def delete_task(self, id):

        deleteTask = self.search_by_id(id)

        return self.task_list.remove(deleteTask)

    def show_tasks(self):

        return self.task_list

    def search_by_id(self, id):

        for task in self.task_list:
            if task.id == id:
                return task
