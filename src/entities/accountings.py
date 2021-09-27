class Accounting:
    def __init__(self):
        self.usage = []
        self.cost_per_tick = 1

    def add_server(self, server):
        self.usage.append(server)

    def calculate_cost_usage(self):
        uptime = 0
        for server in self.usage:
            uptime += server.get_uptime()

        cost = self.cost_per_tick * uptime
        return cost
