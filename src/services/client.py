#client.py
from utils import *
import socket                                   # Importa o módulo do socket

#!/usr/bin/python                               # This is client.py file

sck = socket.socket()                             # Cria um websocket
host = socket.gethostname()                     # Captura a maquina local
port = 1989                                     # Seleciona a porta

sck.connect((host, port))

data = sck.recv(1024) # Recebe a primeira mensagem do servidor
sck.send(input(data.decode()).encode()) # Mostra a mensagem recebida, e já envia a resposta, no caso o username

print('''
                {}
        '''.format((sck.recv(1024)).decode())) # Boas vindas
    
while(True):
    option = input('''
         ---------------------------------------------
        |            1 - TO START GAME                |
        |            2 - TO EXIT GAME                 |
         ---------------------------------------------
        
        |>> Your option:  ''')

    if(try_convert(option)):
        if int(option) == 1:
            # Toda a lógica do jogo
            sck.send('START'.encode())
            print('''
                        Starting game...
                ''')
            cont_operations = 0
            while(cont_operations < 6):
                print ('Equation: {}?'.format(sck.recv(1024).decode()))
                answer = input('Answer: ')
                while(not (try_convert(answer))):
                    print('The value you entered is not an integer.')
                    answer = input('Answer: ')
                sck.send(answer.encode())
                cont_operations = cont_operations + 1

            print(sck.recv(1024).decode())
            break

        elif int(option) == 2:
            # Sair do jogo
            sck.send('EXIT'.encode())
            print(''' 
                        EXITING THE GAME...
                ''')
            sck.close()
            break
        else:
            print('''
                    This option not exists. Try another.
                ''')
    else:
        print('''
                This option not exists. Try another.
            ''')

   
