import uuid


class Job:
    def __init__(self, user, task):
        self.id = uuid.uuid4()
        self.user = user
        self.task = task

    def get_id(self):
        return self.id

    def get_user(self):
        return self.user

    def get_task(self):
        return self.task
