class Conta:

    def __init__(self):
        self._contas = []
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
        existe = self.busca(pessoa.numero, pessoa.cpf)
        if(existe == None):
            self._contas.append(pessoa)
            return True
        
        return False
        '''
        DESCRIPTION
            Verifica se a pessoa está cadastrada, caso ao contrario ela será cadastrada no sistema.
        '''

    def busca(self, numero, cpf):
        for x in self._contas:
            if x.cpf == cpf and x.numero == numero:
                return x
        
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
        Cliente.cont += 1 
        '''
        DESCRIPTION
            Definição da Classe Cliente;
        '''

    def saca(self, valor):
        valor2 = float(valor)
        if valor2 <= self.saldo:
            self.saldo -= valor2
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
        valor2 = float(valor)
        if self.saldo <= 10000 and valor2 <= 10000 - self.saldo :
            self.saldo += valor2
            self.historico.mov.append('Deposito de R$ {}'.format(valor2))
            return True

        else:
            print('Sem limite!')
            return False
        '''
        DESCRIPTION
            Função de Deposito;
        :param valor:
            Variavel do tipo float;
        :return:
            Novo valor após o deposito; 
        '''
    def transfere(self, numero, valor, lista):
        for x in lista:
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
    
    def imprime(self):
        texto = str(self.abertura) + '\n'
        for x in self.mov:
            texto += x + '\n'
        print(texto)
        return texto
        '''
        DESCRIPTION
            Imprime o Histórico
        '''