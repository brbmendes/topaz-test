import sys


def has_input_file(args):
    if len(args) <= 1:
        return False
    return True


def open_file(input_file_text):
    try:
        with open(input_file_text) as f:
            file_input = [line.rstrip('\n') for line in f]
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

    # Controla o ID do último servidor criado, para simular um identity no banco de dados
    last_server_id: 0

    # Obtém o ttask e o umax
    TTASK = int(file.pop(0));
    UMAX = int(file.pop(0));

    new_users_for_tick = []

    # Adiciona os usuários por tick na lista para poder fechar o arquivo.
    for line in file:
        new_users_for_tick.append(int(line))

    # loop principal do programa
    # while True:











    print(new_users_for_tick)
