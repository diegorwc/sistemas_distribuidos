import socket
import re
import configparser
import sys

config = configparser.ConfigParser()
config.read('./config.ini')

print(config[sys.argv[1]]['port'])
host = '127.0.0.1'
port = int(config[sys.argv[1]]['port'])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind((host, port)) 
server_socket.listen() 

print("Servidor inicializado na porta " + str(port))

while True: 
    s, addr = server_socket.accept()
    print(s, addr)
    print('Cliente Conectado:', addr[0], ':', addr[1])
    msg = s.recv(1024)
    msgd = msg.decode()
    print(msgd)
    user = re.search(r'usuario=(.*)&', msgd)
    pw = re.search(r'senha=(.*)', msgd)    
    print(user)
    print(pw)
    response = "HTTP/1.1 401 Unauthorized\n\nNao autorizado"
    if (user is not None and pw is not None):
        if (user.group(1) == 'diego' and pw.group(1) == 'alo'): 
            print('Logged in')
            response = "HTTP/1.1 200 OK\n\nHello World"                                                    
    print(response)    
    try:
        s.send(response.encode())      
        s.close()     
    except:
        print('Erro ao responder.')