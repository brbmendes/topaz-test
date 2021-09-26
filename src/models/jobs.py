import uuid


class Job:
    def __init__(self, user_id, task_id):
        self.id = uuid.uuid4()
        self.user_id = user_id
        self.task_id = task_id

    def get_id(self):
        return self.id

    def get_user_id(self):
        return self.user_id

    def get_task_id(self):
        return self.task_id
