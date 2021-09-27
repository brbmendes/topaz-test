import uuid


class Job:
    def __init__(self, user, task):
        self.__id = uuid.uuid4()
        self.__user = user
        self.__task = task

    def get_id(self):
        return self.__id

    def get_user(self):
        return self.__user

    def get_task(self):
        return self.__task
