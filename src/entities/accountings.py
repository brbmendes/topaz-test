class Accounting:
    def __init__(self):
        self.__usage = []
        self.__cost_per_tick = 1

    def add_server(self, server):
        self.__usage.append(server)

    def calculate_cost_usage(self):
        uptime = 0
        for server in self.__usage:
            uptime += server.get_uptime()

        cost = self.__cost_per_tick * uptime
        return cost
