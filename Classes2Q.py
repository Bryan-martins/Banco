class Conta:

    _total_contas = 0
    __slots__ = ['_numero', '_titular', 'saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo, limite = 10000):
        self._numero = numero
        self._titular = cliente
        self.saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

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
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

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
            print('Sem saldo! ')
            return False
    
    def extrato(self):
        print('Saldo: {} \nConta: {}'.format(self.saldo, self.numero))
        self.historico.mov.append('Tirado o extrato!, saldo de R$ {}'.format(self.saldo))
    
    def transfere(self, contas, valor):
        opc = int(input('Digite a conta para qual vai transferir: '))

        for x in contas:
            if x.numero == opc:     
                res = self.saca(valor)
                if res:
                    res2 = x.deposita(valor)
                    if res2:
                        self.historico.mov.append('Tranferencia para a conta {}, no valor de R$ {} (Saque acima)'.format(x.numero,valor))
                    
                    else:
                        print('la')
                        print('Erro! ')
                        self.deposita(valor)
                else:
                    return False

    def menu(self, contas):
        cont = 1

        while cont != 0:
            print('MENU: ')
            print('1 - Depositar: ')
            print('2 - Sacar: ')
            print('3 - Extrato: ')
            print('4 - Transferir: ')
            print('5 - Historico: ')
            print('0 - Sair: ')
            opc = int(input())

            if opc == 1:
                valor = float(input('Digite o valor: '))
                self.deposita(valor)
                print()
            
            elif opc == 2:
                valor = float(input('Digite o valor: '))
                self.saca(valor)
                print()

            elif opc == 3:
                self.extrato()
                print()
            
            elif opc == 4:
                valor = float(input('Digite o valor: '))
                self.transfere(contas, valor)
                print()
            
            elif opc == 5:
                print('Abertura da conta:', self.historico.abertura)
                for x in range(len(self.historico.mov)):
                    print('-', self.historico.mov[x])
                
                print()
        
            elif opc == 0:
                cont = 0

            else:
                print('Digite uma opção válida! ')
                print()


class Cliente:
    def __init__(self, nome, sn, cpf):
        self._nome = nome
        self._sn = sn
        self._cpf = cpf

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

import datetime

class Historico:
    def __init__(self):
        self.abertura = datetime.datetime.today()
        self.mov = []