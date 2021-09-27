import uuid


class UsedServer:
    def __init__(self, uptime):
        self.__id = uuid.uuid4()
        self.__uptime = uptime

    def get_id(self):
        return self.__id

    def get_uptime(self):
        return self.__uptime
