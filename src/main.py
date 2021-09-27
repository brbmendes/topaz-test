import sys
from math import ceil

from entities.accountings import Accounting
from entities.jobs import Job
from entities.servers import Server
from entities.tasks import Task
from entities.users import User


def has_input_file(args):
    if len(args) <= 1:
        return False
    return True

def open_file(input_file_text):
    try:
        with open(input_file_text) as file_text:
            file_input = [int(new_line.rstrip('\n')) for new_line in file_text]
            return file_input
    except IOError:
        print("Falha ao abrir o arquivo informado.")
        sys.exit()

def update_output(current_output, list_of_active_servers):
    has_started = False
    usage = ""
    if len(list_of_active_servers) <= 0:
        usage = "0"
    else:
        for active_server in list_of_active_servers:
            if not has_started:
                usage = str(len(active_server.get_running_jobs()))
                has_started = True
            else:
                usage += "," + str(len(active_server.get_running_jobs()))

    current_output.append(usage)
    return current_output

def write_output(final_output, final_cost):
    with open("./output/output.txt", 'w') as out_file:
        for output_line in final_output:
            out_file.write(f"{output_line}\n")
        out_file.write(str(final_cost))
    print("\nO arquivo de saída \"output.txt\" foi gerado no caminho \"topaz-test/output/output.txt\"\n")

if __name__ == '__main__':
    has_input_file = has_input_file(sys.argv)
    if not has_input_file:
        print("Por favor informe um arquivo de entrada.")
        sys.exit()

    input_file = sys.argv[1]

    file = open_file(input_file)

    next_server_id = 1

    TTASK = file.pop(0)
    UMAX = file.pop(0)

    new_users_per_tick = file

    active_servers = []
    temporary_active_servers = []
    accounting = Accounting()
    output = []
    while len(active_servers) > 0 or len(new_users_per_tick) > 0:
        current_capacity = 0
        for server in active_servers:
            server.update_tasks_remove_finished()

        for server in active_servers:
            if len(server.get_running_jobs()) > 0:
                temporary_active_servers.append(server)
                current_capacity += UMAX - len(server.get_running_jobs())
                server.update_uptime()
            else:
                accounting.add_server(server)

        active_servers = [] + temporary_active_servers
        temporary_active_servers = []

        if len(new_users_per_tick) > 0:
            new_users = new_users_per_tick.pop(0)
        else:
            new_users = 0

        if new_users > current_capacity:
            number_new_servers = ceil((new_users - current_capacity) / UMAX)
            for number in range(number_new_servers):
                new_server = Server(next_server_id, UMAX)
                next_server_id += 1
                active_servers.append(new_server)

        for user in range(new_users):
            for server in active_servers:
                if server.can_add_job():
                    job = Job(User(), Task(TTASK))
                    server.add_job(job)
                    break

        output = update_output(output, active_servers)

    cost = accounting.calculate_cost_usage()
    write_output(output,cost)
    print('Fim do programa.')
