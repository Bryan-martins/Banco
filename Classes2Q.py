class Conta:

    _total_contas = 0

    def __init__(self):
        self._contas = []
        Conta._total_contas += 1

    def cadastra(self, pessoa):
        existe = self.busca(pessoa.numero, pessoa.cpf)
        if(existe == None):
            self._contas.append(pessoa)
            return True
        
        else:
            return False

    def busca(self, numero, cpf):
        for x in self._contas:
            if x.cpf == cpf and x.numero == numero:
                return x
        
        return None

    def deposita(self, valor):
        if self.saldo <= 10000 and valor <= 10000 - self.saldo :
            self.saldo += valor
            self.historico.mov.append('Deposito de R$ {}'.format(valor))
            return True

        else:
            print('Sem limite!')
            return False

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.mov.append('Saque de R$ {}'.format(valor)) 
            return True
        else:
            return False
    
    def extrato(self):
        print('Saldo: {} \nConta: {}'.format(self.saldo, self.numero))
        self.historico.mov.append('Tirado o extrato!, saldo de R$ {}'.format(self.saldo))
    
    def transfere(self, numero, valor, pessoa):
        for x in self._contas:
            if x.numero == numero:     
                res = pessoa.saca(valor)
                if res:
                    res2 = x.deposita(valor)
                    if res2:
                        pessoa.historico.mov.append('Tranferencia para a conta {}, no valor de R$ {} (Saque acima)'.format(x.numero,valor))
                    
                    else:
                        pessoa.deposita(valor)
                else:
                    return False


class Cliente:

    __slots__ = ['_nome','_numero', '_sn','_cpf', 'saldo', '_limite', '_historico']

    def __init__(self, numero, nome, sn, cpf, saldo, limite = 10000):
        self._numero = numero
        self._nome = nome
        self._sn = sn
        self._cpf = cpf
        self.saldo = saldo
        self._limite = limite
        self._historico = Historico()

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

    @staticmethod
    def get_total_contas():
        return Conta._total_contas

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