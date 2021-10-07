import socket
import configparser
import sys

config = configparser.ConfigParser()
config.read('./gossip.ini')

host = '127.0.0.1'
port = int(config[sys.argv[1]]['port'])

vizinho1 = ('127.0.0.1', config[sys.argv[1]]['vizinho1'])
vizinho2 = ('127.0.0.1', config[sys.argv[1]]['vizinho2'])
vizinhos = list((vizinho1, vizinho2))
# print(vizinhos)
# for v in vizinhos:
#     print(v[1])

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind((host, port)) 
server_socket.listen()
gossip = ''

while True:
    s, addr = server_socket.accept()
    print('Cliente Conectado:', addr[0], ':', addr[1])    
    msg = s.recv(1024)
    if (gossip == msg.decode()):
        continue
    print(msg.decode())
    response = "OK"    
    for v in vizinhos:        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (v[0], int(v[1]))
        client_socket.settimeout(5)
        client_socket.connect(dest)         
        client_socket.send(msg)        
        client_socket.close()
    gossip = msg.decode()
    try:
        s.send(response.encode())      
        s.close()     
    except:
        print('Erro ao responder.')
    