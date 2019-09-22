# coding=utf-8
import logging
import socket
import operator
# manage many of connections
# Nos da capacidades de operar IO no nível do SO, porque sockest nos windows e linux são diferentes e com select este codigo
# ira rodar no mac linux e windows.
import select
#you can use pickle for anything whereas like JSON
import pickle
import time

HEADER_LENGTH = 10
# IP = "192.168.0.111"  # Standard loopback interface address (localhost)
PORT = 1989  # Port to listen on (non-privileged ports are > 1023)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
IP = socket.gethostbyname(local_hostname)

# AF adrees family
# SOCK_STREAM correspond to TCP protocol
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.settimeout(1)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

#irá nos permitir reconectar
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# socket.gethostname() ié basicamente meu localhost
# sockets são 'pontos' 'porta de esntrada' para estabelecer uma conexao e receber ou enviar dados
server_socket.bind((IP, PORT))

# posso passar um valor para criar uma fila.
server_socket.listen()

print(f"Listening on {(IP, PORT)}")

# start manage list of clientes... we have sockest

sockets_list = [server_socket]

# dicionáiro de clientes, socket will be the  key e user data is the value
clients = {}

def receive_message(client_socket):
    try:

        message_header = client_socket.recv(HEADER_LENGTH)

        # se não obtivermos nenhum dado o client fechara a conexao
        if not len(message_header):
            return False

        message_length = int(message_header.decode("utf-8").strip())

        return {"header": message_header, "data": client_socket.recv(message_length)}

    except socket.timeout as err:
        logging.error(err)
    except socket.error as err:
        logging.error(err)


while True:
    # select dot select, takes 3 pramester, read list(sockets we gonna read, sockest we are gonnna read and wirte, sockets we might air on),
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print(f"Accepted new connnection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}")
            '''
            print("---------------------------------------------")
            print("|                 START GAME                |")
            print("|                 EXIT GAME                 |")
            print("---------------------------------------------")
            '''
        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Receive message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

            for client_socket in clients:
                # if client_socket != notified_socket: notificar os outros
                if client_socket != notified_socket:
                    # dizemos que o que queremos enviar pelo socket, como bytes('welcome', 'utf-8')
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]






