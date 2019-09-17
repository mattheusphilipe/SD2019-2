import socket

# manage many of connections
# Nos dá capacidades de operar IO no nível do SO, porque sockest nos windows e linux são diferentes e com select este codigo
# ira rodar no mac linux e windows.
import select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

# AF adrees family
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

