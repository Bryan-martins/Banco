import psycopg2
import threading

conexao = psycopg2.connect(user="postgres",
                                password="122323qwe",
                                host="127.0.0.1",
                                port="5432",
                                database="POOII")
cursor = conexao.cursor()

'''
sql = """CREATE TABLE IF NOT EXISTS Contador(id integer PRIMARY KEY);"""
cursor.execute(sql)
conexao.commit()
insert = """INSERT INTO Contador(ID) VALUES (%s)"""
pessoaaux = '0'
cursor.execute(insert, pessoaaux)
conexao.commit()
'''

class Conta:

    def __init__(self):
        self._contas = []
        self.sinc = threading.Lock()
        '''
        DESCRIPTION
            Definição da Classe Conta    
        '''

    def print(self):
        for x in self._contas:
            print(x.cpf)
            print(x.numero)
            print(' ')

    def cadastra(self, pessoa):
        sql = """CREATE TABLE IF NOT EXISTS Contas (id varchar PRIMARY KEY, nome text NOT NULL, sobrenome text NOT NULL, cpf text NOT NULL, saldo real NOT NULL, limite real NOT NULL);"""
        cursor.execute(sql)
        existe = self.busca(pessoa.numero, pessoa.cpf)
        if(existe == None):
            self._contas.append(pessoa)
            self.sinc.acquire()
            conexao.commit()
            insert = """INSERT INTO Contas(ID, nome, sobrenome, cpf, saldo, limite) VALUES (%s, %s, %s, %s, %s, %s)"""
            pessoaaux = (pessoa.numero, pessoa.nome, pessoa.sn, pessoa.cpf, pessoa.saldo, pessoa.limite)
            cursor.execute(insert, pessoaaux)
            conexao.commit()
            self.sinc.release()
            return True
        
        return False
        '''
        DESCRIPTION
            Verifica se a pessoa está cadastrada, caso ao contrario ela será cadastrada no sistema.
        '''

    def busca(self, numero, cpf):
        conexao.commit()
        self.sinc.acquire()
        cursor.execute("SELECT ID, cpf from Contas")
        self.sinc.release()
        lista = cursor.fetchall()
        lista2 = list(lista)

        #print(int(numero), lista2[0][0])
        for x in lista2:
            if numero == x[0]:
                if cpf == x[1]:
                    return x
        
        conexao.commit()
        return None

    def logar(self, numero, cpf):
        conexao.commit()
        self.sinc.acquire()
        cursor.execute("SELECT * from Contas")
        self.sinc.release()
        lista = cursor.fetchall()
        lista2 = list(lista)

        #print(int(numero), lista2[0][0])
        for x in lista2:
            if numero == x[0]:
                lista3 = x
                return lista3
        
        conexao.commit()
        return None
        '''
            DESCRIPTION
                Verifica se existe alguem cadastrado com o cpf e o numero da conta pesquisado.
            :param numero:
                Variavel do tipo int;
            :param cpf: 
                Variavel do tipo int;
            :return:
                Caso exista alguem cadastrado ele retorna a pessoa que possui os dados pesquisados
                senão ele retorna None;
        '''
    
    def extrato(self):
        print('Saldo: {} \nConta: {}'.format(self.saldo, self.numero))
        self.historico.mov.append('Tirado o extrato!, saldo de R$ {}'.format(self.saldo))

        '''
        DESCRIPTION
            Detalhamento das movimentações bancarias feitas pelo usuario; 
        '''

    def sair(self):
        conexao.commit()

        cursor.close()
        conexao.close()
        
class Cliente:

    cont = 1
    __slots__ = ['_nome','_numero', '_sn','_cpf', 'saldo', '_limite', '_historico']

    def __init__(self, numero, nome, sn, cpf, saldo = 100, limite = 10000):
        self._numero = numero
        self._nome = nome
        self._sn = sn
        self._cpf = cpf
        self.saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self.sinc = threading.Lock()

        '''
        DESCRIPTION
            Definição da Classe Cliente;
        '''

    def saca(self, valor):
        conexao.commit()
        valor2 = float(valor)
        if valor2 <= self.saldo:
            self.saldo -= valor2
            self.sinc.acquire()
            update = '''Update Contas set saldo = %s where id = %s'''
            cursor.execute(update, (self.saldo, self.numero))
            conexao.commit()
            self.sinc.release()
            self.historico.mov.append('Saque de R$ {}'.format(valor2))
            return True
        else:
            return False
        '''
        DESCRIPTION
            Função de saque;
        :param valor:
            Variavel do tipo float;
        :return:
            Novo valor após o saque;
        '''

    def deposita(self, valor):
        conexao.commit()
        '''valor2 = float(valor)
        if self.saldo <= 10000 and valor2 <= 10000 - self.saldo :
            self.saldo += valor2
            self.historico.mov.append('Deposito de R$ {}'.format(valor2))
            return True

        else:
            print('Sem limite!')
            return False
        '''
        valor2 = float(valor)
        if self.saldo <= 10000 and valor2 <= 10000 - self.saldo :
            self.saldo += valor2
            self.historico.mov.append('Deposito de R$ {}'.format(valor2))
            self.sinc.acquire()
            update = '''Update Contas set saldo = %s where id = %s'''
            cursor.execute(update, (self.saldo, self.numero))
            conexao.commit()
            self.sinc.release()
            return True
        '''
        DESCRIPTION
            Função de Deposito;
        :param valor:
            Variavel do tipo float;
        :return:
            Novo valor após o deposito; 
        '''
    def transfere(self, numero, valor):
        conexao.commit()
        cursor.execute("SELECT * from Contas")
        lista3 = cursor.fetchall()
        lista4 = list(lista3)

        '''for x in lista:
            if x.numero == numero and x.numero != self.numero:     
                res = self.saca(valor)
                if res:
                    res2 = x.deposita(valor)
                    if res2:
                        self.historico.mov.append('Tranferencia para a conta {}, no valor de R$ {} (Saque acima)'.format(x.numero,float(valor)))
                        return True

                    else:
                        self.deposita(valor)
                else:
                    return False
        '''
        for x in lista4:
            if x[0] == numero:
                pessoa = x
        
        if pessoa[0] == numero and pessoa[0] != self.numero:
            existe = Cliente(pessoa[0], pessoa[1], pessoa[2], pessoa[3], pessoa[4])
            self.sinc.acquire()    
            res = self.saca(valor)
            if res:
                res2 = existe.deposita(valor)
                if res2:
                    self.historico.mov.append('Tranferencia para a conta {}, no valor de R$ {} (Saque acima)'.format(numero, float(valor)))
                    return True

                else:
                    self.deposita(valor)
            else:
                return False
            self.sinc.release()
        '''
        DESCRIPTION
            Transferencia entre contas;
        '''

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, sn):
        self._sn = sn

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite
    
    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        self._historico = historico

import datetime

class Historico:
    def __init__(self):
        self.abertura = datetime.datetime.today()
        self.mov = []
        '''
        DESCRIPTION
            Definição da Classe Historico    
        '''
    '''
    def imprime(self):
       
        texto = str(self.abertura) + '\n'
        for x in self.mov:
            texto += x + '\n'
        print(texto)
        return texto
    
        DESCRIPTION
            Imprime o Histórico
        '''

import threading

class Cliente_thread(threading.Thread):
    def __init__(self, con, cliente):
        threading.Thread.__init__(self)
        self.cliente = con
        print('Conexão: ', con)

    def run(self):
        cad = Conta()

        cont = 1

        while(cont != 0):

            info = self.cliente.recv(1024).decode()
            lista = info.split("!")

            if (lista[0] == "1"):
                pessoa = Cliente(lista[3], lista[1], lista[2], lista[3])
                if(cad.cadastra(pessoa)):
                    p = "True"
                    self.cliente.send(p.encode())
                else:
                    p = "False"
                    self.cliente.send(p.encode())   

            elif (lista[0] == "2"):
                existe = cad.logar(lista[1], lista[2])
                print( existe[3], existe[4], existe[0])
                if (existe != None):
                    p = "{}!{}!{}!{}".format("True", existe[3], existe[4], existe[0])
                    self.cliente.send(p.encode())
                
                else:
                    p = "{}!{}!{}!{}".format("False", 0, 0, 0)
                    self.cliente.send(p.encode())

            elif (lista[0] == "3"):
                existe = cad.logar(lista[3], lista[2])
                existe2 = Cliente(existe[0], existe[1], existe[2], existe[3], existe[4])
                if(existe2.saca(lista[1]) == True):
                    p = str(existe2.saldo)
                    self.cliente.send(p.encode())
                    print('Saque')
                else:
                    print('Erro!')

            elif (lista[0] == "4"):
                existe = cad.logar(lista[3], lista[2])
                existe3 = Cliente(existe[0], existe[1], existe[2], existe[3], existe[4])
                if(existe3.deposita(lista[1]) == True):
                    p = str(existe3.saldo)
                    self.cliente.send(p.encode())
                    print('Deposito')
                else:
                    print('Erro!')
                
            elif (lista[0] == "5"):
                existe = cad.logar(lista[2], lista[1])
                existe3 = Cliente(existe[0], existe[1], existe[2], existe[3], existe[4])
                texto = existe3.historico.imprime()
                self.cliente.send(texto.encode())
            
            elif (lista[0] == "6"):
                existe = cad.logar(lista[2], lista[1])
                existe4 = Cliente(existe[0], existe[1], existe[2], existe[3], existe[4])
                if(existe4.transfere(lista[3], lista[4]) != False):
                    p = str(existe4.saldo)
                    self.cliente.send(p.encode())
                    print('Tranferencia')
                else:
                    print('Erro!')

            elif (lista[0] == "0"):
                cont = int(lista[1])
                print('Desconexão de :', self.cliente)
                exit()

