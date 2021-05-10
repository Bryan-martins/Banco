class Conta:

    def __init__(self):
        self._contas = []

    def cadastra(self, pessoa):
        for x in self._contas:
            if pessoa.cpf == x.cpf:
                return False
        
        self._contas.append(pessoa)
        return True  

    def busca(self, numero, cpf):
        for x in self._contas:
            if x.cpf == cpf and x.numero == numero:
                return x
        
        return None
    
    def extrato(self):
        print('Saldo: {} \nConta: {}'.format(self.saldo, self.numero))
        self.historico.mov.append('Tirado o extrato!, saldo de R$ {}'.format(self.saldo))

class Cliente:

    cont = 1
    __slots__ = ['_nome','_numero', '_sn','_cpf', 'saldo', '_limite', '_historico']

    def __init__(self, numero, nome, sn, cpf, saldo, limite = 10000):
        self._numero = numero
        self._nome = nome
        self._sn = sn
        self._cpf = cpf
        self.saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Cliente.cont += 1 

    def saca(self, valor):
        valor2 = float(valor)
        if valor2 <= self.saldo:
            self.saldo -= valor2
            self.historico.mov.append('Saque de R$ {}'.format(valor2)) 
            return True
        else:
            return False

    def deposita(self, valor):
        valor2 = float(valor)
        if self.saldo <= 10000 and valor2 <= 10000 - self.saldo :
            self.saldo += valor2
            self.historico.mov.append('Deposito de R$ {}'.format(valor2))
            return True

        else:
            print('Sem limite!')
            return False

    def transfere(self, numero, valor, lista):
        for x in lista:
            if x.numero == numero:     
                res = self.saca(valor)
                if res:
                    res2 = x.deposita(valor)
                    if res2:
                        self.historico.mov.append('Tranferencia para a conta {}, no valor de R$ {} (Saque acima)'.format(x.numero,float(valor)))
                    
                    else:
                        self.deposita(valor)
                else:
                    return False

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