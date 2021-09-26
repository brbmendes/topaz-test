import uuid


class Task:
    def __init__(self, ticks):
        self.id = uuid.uuid4()
        self.ticks = ticks

    def get_id(self):
        return self.id

    def get_ticks(self):
        return self.ticks
