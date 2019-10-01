#client.py
from utils import *

#!/usr/bin/python                               # This is client.py file

import socket                                   # Import socket module

s = socket.socket()                             # Create a socket object
host = socket.gethostname()                # Get local machine name
port = 1989                                    # Reserve a port for your service.

s.connect((host, port))

# print("Conexão feita com sucesso")
data = s.recv(1024) # Recebe a primeira mensagem do servidor
s.send(input(data.decode()).encode()) # Mostra a mensagem recebida, e já envia a resposta, no caso o username

print('''
                {}
        '''.format((s.recv(1024)).decode())) # Boas vindas
    
while(True):
    game_control = input('''
         ---------------------------------------------
        |            1 - TO START GAME                |
        |            2 - TO EXIT GAME                 |
         ---------------------------------------------
        
        |>> Your option:  ''')

    if(try_int(game_control)):
        if int(game_control) == 1:
            # Toda a lógica do jogo
            s.send('START'.encode())
            print('''
                        Starting game...
                ''')
            cont_operations = 0
            while(cont_operations < 6):
                print ('Equation: {}?'.format(s.recv(1024).decode()))
                resp = input('Answer: ')
                while(not (try_int(resp))):
                    print('The value you entered is not an integer.')
                    resp = input('Answer: ')
                s.send(resp.encode())
                cont_operations = cont_operations + 1

            print(s.recv(1024).decode())

        elif int(game_control) == 2:
            # Sair do jogo
            s.send('EXIT'.encode())
            print(''' 
                        EXITING THE GAME...
                ''')
            s.close()
            break
        else:
            print('''
                    This option not exists. Try another.
                ''')
    else:
        print('''
                This option not exists. Try another.
            ''')

   
