import socket
from Classes2Q import *

cad = Conta()

host = 'localhost'
port = 8000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print('Aguardando conexão..')
con, cliente = serv_socket.accept()
print('Conectando..')
print('Aguardando mensagem..')

'''
enviar = ''
while(enviar != 'sair'):
    recebe = con.recv(1024)
    print('Mensagem recebida: '+ recebe.decode())
    enviar = input('Digite uma mensagem para o cliente: ')
    con.send(enviar.encode())
'''

while(True):
    info = con.recv(1024).decode()
    lista = info.split("!")

    if (lista[0] == "1"):
        pessoa = Cliente(str((Cliente.cont)), lista[1], lista[2], lista[3])
        if(cad.cadastra(pessoa)):
            p = "True"
            con.send(p.encode())
        else:
            p = "False"
            con.send(p.encode())   

    elif (lista[0] == "2"):
        existe = cad.busca(lista[1], lista[2])
        if (existe != None):
            p = "True"
            con.send(p.encode())
        
        else:
            p = "False"
            con.send(p.encode())

serv_socket.close()