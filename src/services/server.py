import socket, threading
from utils_old import *

# Aqui a gente define a thread que vai ficar rodando para cada cliente conectado
# Tudo que é definido aqui dentro será para tratar exclusivamente 1 cliente
def run(conn):
    conn.send('Type your name to begin: '.encode())
    conn.send('Welcome {}!'.format(conn.recv(1024).decode()).encode())
    data = conn.recv(1024) # receber informacao

    LAST_RESULT_EQUATION = None
    RIGHT_ANSWER_QTD = 0
    WRONG_ANSWER_QTD = 0
    client_response = []
        
    if data.decode() == 'START':
        # Logica de início do jogo
        info_client = {
            'operations': [],
            'answersClient': [],
            'answersServer': [],
            'wrongAnswers': 0,
            'rightAnswers': 0
        }
        
        while(len(info_client['operations']) < 6):
            equacao = fun_equacao() # Cria as equações e repostas
            LAST_RESULT_EQUATION = equacao[1] # Resultado da equação
            conn.send(equacao[0].encode())
            response = conn.recv(1024).decode()
            info_client['operations'].append(equacao[0])
            info_client['answersServer'].append(equacao[1])
            info_client['answersClient'].append(response)
            if int(response) == LAST_RESULT_EQUATION:
                info_client['rightAnswers'] = info_client['rightAnswers'] + 1
            else:
                info_client['wrongAnswers'] = info_client['wrongAnswers'] + 1

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
                      
                '''.format(info_client['rightAnswers'], info_client['wrongAnswers'], info_client['answersClient'], info_client['answersServer']).encode())
        
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
with socket.socket() as sock: # Fazemos a ligacao TCP
    # Faz com que o endereço possa ser reutilizado logo a seguir a fechar o servidor
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((host, port))
    sock.listen(5) # Servidor ativo
    print('Server started at {}:{}\n'.format(host, port))
    while True:
        conn, addr = sock.accept() # Aguarda até que algum cliente se conecte
        threading.Thread(target=run, args=(conn,)).start() # Conexão é passada pra thread e já é iniciada
        print("Client connected: {}".format(addr)) #Só pra mostrar os dados do cliente
        conns.add(conn) # Adiciona essa conexão ao set de conexão
        print('''Connected hosts:: {}
        '''.format(conns))
        
