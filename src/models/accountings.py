class Accounting:
    def __init__(self):
        self.usage = []

    def add_server(self, server):
        self.usage.append(server)

    def get_usage(self):
        return self.usage
