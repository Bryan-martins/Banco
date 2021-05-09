import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from Classes2Q import *
from Tela_cadastro import Tela_cadastro
from Tela_Menu import Tela_menu
from Tela_Transferir import Tela_transferir
from Tela_Usuario import Tela_usuario
from Tela_Login import Tela_login
from Tela_Saque import Tela_Saque
from tela_Extrato import Tela_extrato
from Tela_Deposito import Tela_Deposito

class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(640, 515)

        self.QStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_menu()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_usuario = Tela_usuario()
        self.tela_usuario.setupUi(self.stack2)

        self.tela_transferir = Tela_transferir()
        self.tela_transferir.setupUi(self.stack3)

        self.tela_login = Tela_login()
        self.tela_login.setupUi(self.stack4)


        self.QStack.addWidget(self.stack0)
        self.QStack.addWidget(self.stack1)
        self.QStack.addWidget(self.stack2)
        self.QStack.addWidget(self.stack3)
        self.QStack.addWidget(self.stack4)

class Main(QMainWindow, Ui_Main):


    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Conta()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaLogin)
        
        self.tela_login.pushButton.clicked.connect(self.voltar)
        self.tela_login.pushButton_2.clicked.connect(self.BotaoLogar)

        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar)
        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
    
    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEdit.text()
        CPF = self.tela_cadastro.lineEdit_2.text()
        Sobrenome = self.tela_cadastro.lineEdit_5.text()
        self.tela_cadastro.lineEdit.setText('')
        self.tela_cadastro.lineEdit_2.setText('')
        self.tela_cadastro.lineEdit_5.setText('')

        if not(nome == '' or CPF == '' or Sobrenome == ''):
            p = Cliente(str(Cliente.cont), nome, Sobrenome, CPF, 100.0)

            if(self.cad.cadastra(p)):
                QMessageBox.information(None, 'POOII', 'Cadastrado com sucesso! ')
            
            else:
                QMessageBox.information(None, 'POOII', 'O CPF informado já está cadastrado! ')
            
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valores devem ser preenchidos! ')
        
        self.QStack.setCurrentIndex(0)

    def BotaoLogar(self):
        numero = self.tela_login.lineEdit.text()
        cpf = self.tela_login.lineEdit_2.text()
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')
        pessoa = self.cad.busca(numero, cpf)
        if (pessoa != None):
            self.menu(pessoa)
            
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valores devem ser preenchidos! ')

        return None

    def menu(self, pessoa):
        self.QStack.setCurrentIndex(2)
        self.tela_usuario.pushButton_3.clicked.connect(lambda:self.botaoTranferir(pessoa))
        self.tela_usuario.pushButton_5.clicked.connect(self.voltar)
        self.tela_usuario.pushButton.clicked.connect(self.botaoSacar)
        self.tela_usuario.pushButton_2.clicked.connect(self.botaoDepositar)
        return None
        
    def botaoSacar(self, pessoa):
        valor = self.Tela_Saque.lineEdit.setText('')
        saldoAntigo = self.Tela_Saque.lineEdit_2.setText(str(pessoa.saldo))
        pessoa.saca(valor)
        novoSaldo = self.Tela_Saque.lineEdit_3.setText(str(pessoa.saldo))
        self.Tela_Deposito.pushButton.clicked.connect(self.voltar2)

    def botaoDepositar(self, pessoa):
        valorDeposidado = self.Tela_Deposito.lineEdit.setText('')
        self.Tela_Deposito.lineEdit_2.setText('')
        self.Tela_Deposito.lineEdit_3.setText('')
        self.Tela_Deposito.pushButton.clicked.connect(self.voltar2)

    def botaoTranferir(self, pessoa):
        self.QStack.setCurrentIndex(3)
        self.tela_transferir.lineEdit.setText('')
        self.tela_transferir.lineEdit_2.setText('')
        self.tela_transferir.lineEdit_3.setText(str(pessoa.saldo))
        self.tela_transferir.pushButton.clicked.connect(self.voltar2)
        self.tela_transferir.pushButton_2.clicked.connect(lambda:self.botaoTranferir2(pessoa))
        return None

    def botaoTranferir2(self, pessoa):
        numero = self.tela_transferir.lineEdit.text()
        valor = self.tela_transferir.lineEdit_2.text()
        pessoa.transfere(numero, valor, self.cad._contas)
        self.tela_transferir.lineEdit_3.setText(str(pessoa.saldo))
        return None

    def voltar(self):
        self.QStack.setCurrentIndex(0)
        return None

    def voltar2(self):
        self.QStack.setCurrentIndex(2)
        return None

    def abrirTelaCadastro(self):
        self.QStack.setCurrentIndex(1)
        return None
    
    def abrirTelaLogin(self):
        self.QStack.setCurrentIndex(4)
        return None
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
