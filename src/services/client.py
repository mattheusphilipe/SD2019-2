# coding=utf-8
# como tratar quando excedemos o buffer, cooo lidar com sockets que excedeam o buffer e continuar com a conexão aberta
import socket
import errno
import sys
from utils import *

HEADER_LENGTH = 10
PORT = 1989


local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
# IP = "127.0.0.1" # Standard loopback interface address (localhost)
IP = socket.gethostbyname(local_hostname) # para conectar no servidor que você estiver executando
# IP = "192.168.56.1"

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((IP, PORT))
except Exception as e:
    print("Cannot connect to the server:", e)
print("Connected")


client_socket.setblocking(False)

username = encode_decode(my_username, 1)
username_header = encode_decode(f"{len(username): < {HEADER_LENGTH}}", 1)
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")

    if message:
        message = encode_decode(message, 1)
        message_header = encode_decode(f"{len(message):< {HEADER_LENGTH}}", 1)
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
