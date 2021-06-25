import socket
from Classes2Q import *

host = 'localhost'
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)

print('Aguardando conexão..')
while True:
    serv_socket.listen(1)
    con, cliente = serv_socket.accept()
    newthread = Cliente_thread(con, cliente)
    newthread.start()

print('Conectando..')
print('Aguardando mensagem..')

