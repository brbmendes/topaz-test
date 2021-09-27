class Accounting:
    def __init__(self):
        self.__usage = []
        self.__cost_per_tick = 1

    def get_servers(self):
        return self.__usage

    def add_server(self, server):
        self.__usage.append(server)

    def get_cost_per_tick(self):
        return self.__cost_per_tick

    def set_cost_per_tick(self, new_cost):
        self.__cost_per_tick = new_cost

    def calculate_cost_usage(self):
        uptime = 0
        for server in self.__usage:
            uptime += server.get_uptime()

        cost = self.__cost_per_tick * uptime
        return cost
