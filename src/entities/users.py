import uuid


class User:
    def __init__(self):
        self.id = uuid.uuid4()

    def get_id(self):
        return self.id
