import uuid


class User:
    def __init__(self):
        self.__id = uuid.uuid4()

    def get_id(self):
        return self.__id
