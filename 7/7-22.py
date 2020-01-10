# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/r7BQY/bankovskiie-schieta

# Банковские счета


def count_income(sum, percent):
    return sum * percent // 100 if sum > 0 else 0


def handle_command(command, clients):
    op = command[0]

    if op == 'DEPOSIT':
        client = command[1]
        summa = int(command[2])
        clients[client] = clients.get(client, 0) + summa

    elif op == 'INCOME':
        percent = int(command[1])
        for client in clients:
            clients[client] += count_income(clients[client], percent)

    elif op == 'BALANCE':
        client = command[1]
        print(clients[client]) if client in clients else print('ERROR')

    elif op == 'TRANSFER':
        client_from = command[1]
        client_to = command[2]
        summa = int(command[3])
        clients[client_from] = clients.get(client_from, 0) - summa
        clients[client_to] = clients.get(client_to, 0) + summa

    else:   # op == 'WITHDRAW':
        client = command[1]
        summa = int(command[2])
        clients[client] = clients.get(client, 0) - summa


clients = {}

with open('input.txt', 'r') as finput:
    for line in finput:
        command = line.split()
        handle_command(command, clients)
