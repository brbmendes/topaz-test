import uuid


class UsedServer:
    def __init__(self, uptime):
        self.id = uuid.uuid4()
        self.uptime = uptime

    def get_id(self):
        return self.id

    def get_uptime(self):
        return self.uptime
