import uuid


class Task:
    def __init__(self, ticks):
        self.__id = uuid.uuid4()
        self.__ticks = ticks

    def get_id(self):
        return self.__id

    def get_ticks(self):
        return self.__ticks

    def decrement_tick(self):
        self.__ticks -= 1
