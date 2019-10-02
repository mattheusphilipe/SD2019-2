# coding=utf-8
# como tratar quando excedemos o buffer, cooo lidar com sockets que excedeam o buffer e continuar com a conexão aberta
import socket
import errno
import sys
import time
from utils import *

HEADER_LENGTH = 10
PORT = 1989
LOCAL_HOSTNAME = socket.gethostname()
IP = socket.gethostbyname(LOCAL_HOSTNAME)
MAX_BYTES_TO_RECEIVE = 2048
TIMEOUT_MATCH = 60  # 1 min
QTD_OPERATIONS = 6
MAX_LENGTH_MESSAGE = 12

first_message = True
the_time = 0
elapsed_time = 0
message_length = 0

inputText = '''
                                       ---------------------------------------------
                                       |            START - TO START GAME            |
                                       |            EXIT - TO EXIT GAME              |
                                       ---------------------------------------------
                                       |>> Your option:  '''

MY_USERNAME = input("Digite seu Nome: ")

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    print(f"Conectado com sucesso em: {(IP, PORT)}!")
except socket.error as e:
    print(f"Não foi possível conectar no servidor: {(IP, PORT)}! ", e)
    sys.exit(1)

# modo do socket não bloqueante para não esperar a conclusão de uma operação.
client_socket.setblocking(False)

username = encode_decode(MY_USERNAME, 1)
username_header = encode_decode(f"{len(username): < {HEADER_LENGTH}}", 1)
client_socket.send(username_header + username)

message = None

while True:
    if first_message:
        the_time = time.time()
        elapsed_time = 0
        while True:
            checking_message = str(input(inputText)).upper()
            print("\n")
            if checking_message == "EXIT":
                message = False
                client_socket.close()
                break
            elif checking_message == "START":
                message = checking_message
                break

            print("Erro! Digite START ou EXIT")

        if message:
            message = encode_decode(message, 1)
            message_header = encode_decode(f"{len(message):< {HEADER_LENGTH}}", 1)
            client_socket.send(message_header + message)

        first_message = False

    try:
        # while elapsed_time < TIMEOUT_MATCH and message_length < MAX_LENGTH_MESSAGE:
        while True:
            elapsed_time = time.time() - the_time
            # recebendo coisas
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Conexão fechada pelo servidor")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message = client_socket.recv(MAX_BYTES_TO_RECEIVE).decode("utf-8")
            message_length = len(message)

            print(f"{username} > {message}")  # trocar username por servidor

            # Quando mostrar o resultado fecha a partida atual
            if message_length > MAX_LENGTH_MESSAGE:
                first_message = True
                message_length = 0
                break

            # Se esgotou o tempo finaliza a partida atual
            if elapsed_time > TIMEOUT_MATCH:
                print("Tempo esgotado")
                first_message = True
                message_length = 0
                break

            message = input(f"{MY_USERNAME} > ")

            while not int_float(message, 2):
                print("Digite apenas números, durante a partida, ou EXIT para sair")
                message = input(f"{MY_USERNAME} > ")

                if message.upper() == "EXIT":
                    print('GAME OVER')
                    client_socket.close()
                    break

            if message:
                message = encode_decode(message, 1)
                message_header = encode_decode(f"{len(message):< {HEADER_LENGTH}}", 1)
                client_socket.send(message_header + message)

    except IOError as excepting:
        if excepting.errno != errno.EAGAIN and excepting.errno != errno.EWOULDBLOCK:
            print('Reading error', str(excepting))
            sys.exit(1)
        continue
    except Exception as excepting:
        print('General Error', str(excepting))
        sys.exit(1)

    except KeyboardInterrupt:
        print('Interrupted.')
        client_socket.close()
        break
