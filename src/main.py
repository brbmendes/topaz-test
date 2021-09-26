import sys

from src.entities.accountings import Accounting
from src.entities.jobs import Job
from src.entities.servers import Server
from src.entities.tasks import Task
from src.entities.users import User


def has_input_file(args):
    if len(args) <= 1:
        return False
    return True


def open_file(input_file_text):
    try:
        with open(input_file_text) as file_text:
            file_input = [new_line.rstrip('\n') for new_line in file_text]
            return file_input
    except IOError:
        print("Falha ao abrir o arquivo informado.")
        sys.exit()


if __name__ == '__main__':
    # Testa se foi informado um arquivo de entrada
    has_input_file = has_input_file(sys.argv)
    if not has_input_file:
        print("Por favor informe um arquivo de entrada.")
        sys.exit()

    input_file = sys.argv[1]

    # Tenta abrir e ler o arquivo de entrada
    file = open_file(input_file)

    # Controla o ID do próximo servidor, para simular um identity no banco de dados
    next_server_id = 1

    # Obtém o ttask e o umax
    TTASK = int(file.pop(0))
    UMAX = int(file.pop(0))

    new_users_per_tick = []

    # Adiciona os usuários por tick na lista para poder fechar o arquivo.
    for line in file:
        new_users_per_tick.append(int(line))

    active_servers = []
    inactive_servers = []
    temporary_switch_servers = []
    accounting = Accounting()

    # loop principal do programa
    while len(active_servers) > 0 or len(new_users_per_tick) > 0:
        for server in active_servers:
            # atualiza uptime
            server.update_uptime()

            # Finaliza os jobs correntes e atualiza as tasks
            server.update_tasks_remove_finished()

            # finaliza servers e manda pro acounting
            if len(server.running_jobs) > 0:
                temporary_switch_servers.append(server)
            else:
                inactive_servers.append(server)
                accounting.add_server(server)

        active_servers = [] + temporary_switch_servers
        temporary_switch_servers = []

        # distribui a carga de trabalho
        new_users = new_users_per_tick.pop(0)

        for user in range(new_users):
            if len(active_servers) <= 0:
                new_server = Server(next_server_id, UMAX)
                next_server_id += 1
                job = Job(User(), Task(TTASK))
                new_server.add_job(job)
                active_servers.append(new_server)
            else:
                for server in active_servers:
                    if server.can_add_job:
                        job = Job(User(), Task(TTASK))
                        server.add_job(job)
                        break
                    else:
                        new_server = Server(next_server_id, UMAX)
                        next_server_id += 1
                        job = Job(User(), Task(TTASK))
                        new_server.add_job(job)
                        active_servers.append(new_server)
                        break



    # Quando chega aqui, deve ter acabado tudo
    # falta calcular o accounting


    print('fim do programa')