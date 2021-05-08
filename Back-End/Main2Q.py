from Classes2Q import *

contas = []
cont = 1
cont1 = 0

print('Bem vindo! ')
while cont != 0:
    opc = int(input('1 - Logar || 2 - Cadastrar || 0 - Sair\n'))
    if opc == 1:
        numero = int(input('Digite o numero da conta: '))
        cpf = input('Digite o cpf(000000000-00): ')
        for x in contas:
            if x.numero == numero and x.titular.cpf == cpf:
                x.menu(contas)
        else:
            print()

    elif opc == 2:
        a = input('Digite seu nome: ')
        a2 = input('Digite seu sobrenome: ')
        a3 = input('Digite seu cpf: ')
        cliente = Cliente(a, a2, a3)
        cont1 += 1
        conta = Conta(cont1, cliente, 0.0)
        conta.get_total_contas()
        contas.append(conta)

        print()
        print('Número da conta: ', contas[cont1 - 1].numero)
        print('Senha da conta: ', contas[cont1 - 1].titular.cpf)

    elif opc == 3:
        print()
        print('Contas no sistema: ', Conta.get_total_contas())
        print()
        
        for x in contas:
            print(x.numero)
            print(x.titular.cpf)
            print(x.saldo)

    elif opc == 0:
        print()
        print('Sistema finalizando ')
        cont = 0

    else:
        print('Erro! ')
