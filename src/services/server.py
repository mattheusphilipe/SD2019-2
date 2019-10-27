# coding=utf-8
import logging
import socket
import sys
import time

from utils import *
# manage many of connections
# Nos da capacidades de operar IO no nível do SO, porque sockest nos windows e linux são diferentes e com select este codigo
# ira rodar no mac linux e windows.
import select

local_hostname = socket.gethostname()
IP = socket.gethostbyname(local_hostname)
HEADER_LENGTH = 10
PORT = 1989  # Port to listen on (non-privileged ports are > 1023)
TIMEOUT = 30  # número de segundos para aguardar antes de interromper o monitoramento, se nenhum canal estiver ativo.
QTD_OPERATION = 6
roundNumber = 0
allNotified = 0

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # irá nos permitir reconectar
    server_socket.bind((IP, PORT))  # fazer a ligação do socket ao endereço IP + PORTA
    server_socket.listen(15)  # Esperando conexõe para esse socket
    server_socket.setblocking(
        True)  # socket no modo de bloqueio, o controle so é retornado ao meu programa após a conclusão da operação em curso.
    server_socket.settimeout(0.5)
    print(f"Listening on {(IP, PORT)}")

except socket.timeout as e:
    print(e)
    sys.exit(1)
except socket.error as e:
    print(e)
    sys.exit(1)

sockets_list = [server_socket]

clients = {}  # dicionário de clientes, socket será a chave e a o usuário será o valor da chave (pega os dados do usuário)
client_response = {}  # dicionário para armazenar a estrutura do jogo do usuário (armazena dados do usuário)
message = None
round = {}
qtdFinished = 0
user = None
lastOne = {}
roundEquation = round_structure()
the_time = 0
elapsed_time = 0
ranking_list = []


def receive_message(client_sckt):
    try:
        message_header = client_sckt.recv(HEADER_LENGTH)
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
    try:
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list, TIMEOUT)
        if not (read_sockets or exception_sockets):
            print('Canal de dados vazio')
            continue
    except select.error as e:
        print(e)
        break
    except socket.error as e:
        print(e)
        break

    elapsed_time = time.time() - the_time

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
                    'rightAnswers': 0,
                    'roundNumberClient': 0,
                    'timeRound': [],
                    'clientName': encode_decode(user['data'], 2)
                }

            for client_socket in list(clients):
                if client_socket == notified_socket:

                    message = receive_message(notified_socket)

                    if message is False:
                        print(f"Conexão fechada por {encode_decode(clients[notified_socket]['data'], 2)}")
                        sockets_list.remove(notified_socket)
                        del clients[notified_socket]
                        continue

                    user = clients[notified_socket]
                    print(f"Mensagem recebida de {encode_decode(user['data'], 2)}: {encode_decode(message['data'], 2)}")

                    client_operation_length = len(client_response.get(notified_socket)['answers'])

                    if client_operation_length <= QTD_OPERATION and client_response.get(notified_socket)[
                        'roundNumberClient'] < 7:
                        answer = encode_decode(message['data'], 2)

                        if answer != "START":
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

                        currentOperation = roundEquation[client_response.get(notified_socket)['roundNumberClient']] \
                            .get('operation')
                        currentResult = roundEquation[client_response.get(notified_socket)['roundNumberClient']] \
                            .get('result_operation')

                        client_socket.send(
                            user['header'] + user['data'] + message['header'] + bytes(f"{currentOperation} = ?",
                                                                                      "utf-8")
                        )

                        client_response.get(notified_socket)['result_operation'].append(currentResult)
                        client_response.get(notified_socket)['operations'].append(
                            f"{currentOperation}: {currentResult}")
                        client_response.get(notified_socket)['timeRound'].append(elapsed_time)
                        client_response.get(notified_socket)['roundNumberClient'] += 1
                    else:

                        the_score = bytes(
                            '''
                                                ----------------------
                                               |        SCORE:        |
                                               |                      |
                                               |  Right answers: {}    |
                                               |  Wrong answers: {}    |
                                               |                      |
                                                ----------------------
    
                                            Your answers: {}  
                                            Right answers: {}   
                                            Operations: \n\t\t\t\t\t\t\t{}
                                            RoundTime: \n\t\t\t\t\t\t\t{}
    
                                            '''.format(client_response.get(notified_socket)['rightAnswers'],
                                                       client_response.get(notified_socket)['wrongAnswers'],
                                                       client_response.get(notified_socket)['answers'],
                                                       client_response.get(notified_socket)['result_operation'],
                                                       "\n\t\t\t\t\t\t\t".join([str(elem) for elem in
                                                                                client_response.get(notified_socket)[
                                                                                    'operations']]),
                                                       "\n\t\t\t\t\t\t\t".join([f"{time.ctime(elem)}".split()[-2] for elem in
                                                                    client_response.get(notified_socket)[
                                                                        'timeRound']])
                                                       )
                            , "utf-8")

                        client_socket.send(user['header'] + user['data'] + message['header'] + the_score)
                        qtdFinished += 1
                        allNotified += 1
                        if len(client_response) == 1:
                            lastOne = clients.get(notified_socket)

                        create_ranking_time(client_response.get(notified_socket), ranking_list)
                        client_response.pop(notified_socket)

    if qtdFinished > 0:
        for client_socket in list(clients):

            if client_socket not in client_response and client_socket != lastOne:
                remainClients = f"Jogadores restantes: {len(client_response)}"
                client_socket.send(user['header'] + user['data'] + message['header'] + bytes(remainClients, "utf-8"))

            if len(client_response) == 0:
                qtdFinished = 0

    if allNotified == len(clients):

        for client_socket in list(clients):
            scoreboard = '''
                                    ----------------------
                                   |        RANKING:      |
                                   |                      |
                                   |>  Winner: {}
                                   |                      |
                                    ----------------------

                                 \n\t\t\t\t\t\t\t{}

                                '''.format(ranking_list[0][0],
                                           "\n\t\t\t\t\t\t\t".join(
                                               [str(elem[0] + ': ' + f"{elem[1]}" + ', ' + f"{time.ctime(elem[2])}".split()[-2].split()[-1]) for elem in ranking_list]))

            client_socket.send(
                user['header'] + user['data'] + message['header'] + bytes("TODOS FINALIZARAM A PARTIDA \n" + scoreboard,
                                                                          "utf-8"))
        allNotified = 0

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]
