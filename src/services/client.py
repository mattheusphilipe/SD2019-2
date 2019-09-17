# coding=utf-8
# como tratar quando excedemos o buffer, cooo lidar com sockets que excedeam o buffer e continuar com a conexão aberta
import socket
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1989

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username): < {HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")

    if message:
        print(f"Trying to connect to server {(IP, PORT)}")
        message = message.encode("utf-8")
        message_header = f"{len(message):< {HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)

    try:
        while True:
            # recebendo coisas
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Conexão fechada pelo servidor")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")
            print(f"{username} > {message}")

    except IOError as excepting:
        if excepting.errno != errno.EAGAIN and excepting.errno != errno.EWOULDBLOCK:
            print('Reading error', str(excepting))
            sys.exit()
        continue
    except Exception as excepting:
        print('General Error', str(excepting))
        sys.exit()