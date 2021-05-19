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

cont = 1

while(cont != 0):

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
            p = "{}!{}!{}!{}".format("True", existe.cpf, existe.saldo, existe.numero)
            con.send(p.encode())
        
        else:
            p = "{}!{}!{}!{}".format("False", 0, 0, 0)
            con.send(p.encode())

    elif (lista[0] == "3"):
        existe = cad.busca(lista[3], lista[2])
        if(existe.saca(lista[1]) == True):
            p = str(existe.saldo)
            con.send(p.encode())
            print('Saque')
        else:
            print('Erro!')

    elif (lista[0] == "4"):
        existe = cad.busca(lista[3], lista[2])
        if(existe.deposita(lista[1]) == True):
            p = str(existe.saldo)
            con.send(p.encode())
            print('Deposito')
        else:
            print('Erro!')

    elif (lista[0] == "5"):
        existe = cad.busca(lista[2], lista[1])
        texto = existe.historico.imprime()
        con.send(texto.encode())

    elif (lista[0] == "6"):
        existe = cad.busca(lista[2], lista[1])
        if(existe.transfere(lista[3], lista[4], cad._contas) != False):
            p = str(existe.saldo)
            con.send(p.encode())
            print('Tranferencia')
        else:
            print('Erro!')

    elif (lista[0] == "0"):
        cont = int(lista[1])
        print('Encerrando server ')

serv_socket.close()
exit()