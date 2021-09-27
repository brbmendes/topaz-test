import uuid


class Task:
    def __init__(self, ticks):
        """Creates the task.

        Keyword arguments:
        ticks -- basic unit of time for the simulation
        """
        self.__id = uuid.uuid4()
        self.__ticks = ticks

    def get_id(self):
        return self.__id

    def get_ticks(self):
        return self.__ticks

    def decrement_ticks(self):
        self.__ticks -= 1
