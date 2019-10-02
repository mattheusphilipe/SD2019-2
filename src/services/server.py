# coding=utf-8
import logging
import socket
import sys

from utils import *
# manage many of connections
# Nos da capacidades de operar IO no nível do SO, porque sockest nos windows e linux são diferentes e com select este codigo
# ira rodar no mac linux e windows.
import select

local_hostname = socket.gethostname()
IP = socket.gethostbyname(local_hostname)
HEADER_LENGTH = 10
PORT = 1989  # Port to listen on (non-privileged ports are > 1023)

QTD_OPERATION = 6

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.settimeout(5)

    # irá nos permitir reconectar
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP, PORT))
    server_socket.listen(15)
    print(f"Listening on {(IP, PORT)}")

except socket.error as e:
    print(e)
    sys.exit(1)

# start manage list of clientes... we have sockest

sockets_list = [server_socket]
# dicionário de clientes, socket será a chave e a o usuário será o valor da chave
clients = {}
client_response = {}
message = None


def receive_message(client_sckt):
    try:
        message_header = client_sckt.recv(HEADER_LENGTH)
        # se não obtivermos nenhum dado o client fechara a conexao ?
        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())

        return {
            "header": message_header,
            "data": client_sckt.recv(message_length)
        }

    except socket.timeout as err:
        logging.error(err)
    except socket.error as err:
        logging.error(err)


while True:
    # select dot select, takes 3 pramester, read list(sockets we gonna read, sockest we are gonnna read and wirte,
    try:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    except select.error as e:
        print(e)
        break
    except socket.error as e:
        print(e)
        break

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(
                f"Nova conexão de {client_address[0]}:{client_address[1]}@{user['data'].decode('utf-8')}")

        else:

            if notified_socket not in client_response:
                client_response[notified_socket] = {
                    'operations': [],
                    'answers': [],
                    'result_operation': [],
                    'wrongAnswers': 0,
                    'rightAnswers': 0
                }

            for client_socket in list(clients):
                if client_socket == notified_socket:
                    equation = fun_equacao()
                    message = receive_message(notified_socket)

                    if message is False:
                        print(f"Conexão fechada por {encode_decode(clients[notified_socket]['data'], 2)}")
                        sockets_list.remove(notified_socket)
                        del clients[notified_socket]
                        continue

                    user = clients[notified_socket]
                    print(f"Mensagem recebida de {encode_decode(user['data'], 2)}: {encode_decode(message['data'], 2)}")

                    client_operation_length = len(client_response.get(notified_socket)['answers'])

                    if client_operation_length <= QTD_OPERATION:
                        answer = encode_decode(message['data'], 2)

                        if answer != "START":
                            # frescura se estiver dando problema excluir
                            last_operator = client_response.get(notified_socket)['operations'][-1].split()[1]
                            client_response.get(notified_socket)['answers'].append(answer)

                            if last_operator == '/':
                                switch_convert = float(answer)
                            else:
                                switch_convert = int(answer)

                            if switch_convert == client_response.get(notified_socket)['result_operation'][-1]:
                                client_response.get(notified_socket)['rightAnswers'] += 1
                            else:
                                client_response.get(notified_socket)['wrongAnswers'] += 1
                        # dizemos que o que queremos enviar pelo socket, como bytes('welcome', 'utf-8')
                        client_socket.send(
                            user['header'] + user['data'] + message['header'] + bytes(f"{equation[0]} = ?", "utf-8")
                        )

                        client_response.get(notified_socket)['result_operation'].append(equation[1])
                        client_response.get(notified_socket)['operations'].append(f"{equation[0]}: {equation[1]}")
                    else:
                        client_socket.send(user['header'] + user['data'] + message['header'] + bytes(
                            f"{client_response[notified_socket]} \n END GAME BITCH \n ", "utf-8"))
                        client_response.pop(notified_socket)

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
