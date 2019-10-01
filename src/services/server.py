import socket, threading
from utils import *


# Aqui a gente define a thread que vai ficar rodando para cada cliente conectado
# Tudo que é definido aqui dentro será para tratar exclusivamente 1 cliente
def run(conn):
    conn.send('Type your name to begin: '.encode())
    conn.send('Welcome {}!'.format(conn.recv(1024).decode()).encode())
    data = conn.recv(1024)                                          # receber informacao

    LAST_RESULT_EQUATION = None
    RIGHT_ANSWERS = 0
    WRONG_ANSWERS = 0
    client_response = []
        
    if data.decode() == 'START':
        # Logica de início do jogo
        client = {
            'operations': [],
            'answers_client': [],
            'answers_server': [],
            'wrong_answers': 0,
            'right_answers': 0
        }
        
        while(len(client['operations']) < 6):
            equation = create_equation()                          # Cria as equações e repostas
            LAST_RESULT_EQUATION = equation[1]                      # Resultado da equação
            conn.send(equation[0].encode())
            response = conn.recv(1024).decode()
            client['operations'].append(equation[0])
            client['answers_server'].append(equation[1])
            client['answers_client'].append(response)
            if int(response) == LAST_RESULT_EQUATION:
                client['right_answers'] = client['right_answers'] + 1
            else:
                client['wrong_answers'] = client['wrong_answers'] + 1

        conn.send('''
                    ----------------------
                   |        SCORE:       |
                   |                      |
                   |  Right answers: {}    |
                   |  Wrong answers: {}    |
                   |                      |
                    ----------------------
                    
                Your answers: {}  
                Right answers: {}   
                      
                '''.format(client['right_answers'], client['wrong_answers'], client['answers_client'], client['answers_server']).encode())

        conns.remove(conn)
        conn.close()
        print('''Connected hosts: {}
        '''.format(conns))
      
    elif data.decode() == 'EXIT':
        conns.remove(conn)
        conn.close()
        print('''Connected hosts: {}
        '''.format(conns))


# É como se fosse nosso array de conexões, só pro server ter controle, e você também ;)
conns = set() 

# Capturamos o host, que no caso é a nossa propria máquina
host = socket.gethostname()
port = 1989
with socket.socket() as sock:                                       # Fazemos a ligacao TCP
    # Faz com que o endereço possa ser reutilizado logo a seguir a fechar o servidor
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((host, port))
    sock.listen(15)                                                 # Servidor ativo
    print('Server started at {}:{}'.format(host, port))
    while True:
        conn, addr = sock.accept()                                  # Aguarda até que algum cliente se conecte
        threading.Thread(target=run, args=(conn,)).start()          # Conexão é passada pra thread e já é iniciada
        print("Client connected: {}".format(addr))                  #Só pra mostrar os dados do cliente
        conns.add(conn)                                             # Adiciona essa conexão ao set de conexão
        print('''Connected hosts:: {}
        '''.format(conns))
        
