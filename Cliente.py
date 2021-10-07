import socket 
import sys

def Main(): 

    import configparser

    config = configparser.ConfigParser()
    config.read('./gossip.ini')

    host = '127.0.0.1'
    port = int(config[sys.argv[1]]['port'])
    
    msg = config[sys.argv[1]]['msg']

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host, port) 

    client_socket.settimeout(5)
    client_socket.connect(dest)

    client_socket.send(msg.encode('ascii'))

    try:
        resposta, servidor = client_socket.recvfrom(1024)
        print('Resposta do Servidor: ', resposta.decode())
    except: 
        print('Ocorreu um erro...')

    client_socket.close() #Fecha a conexão com o servidor

if __name__ == '__main__': 
	Main()