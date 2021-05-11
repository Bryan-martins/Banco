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
from tela_Historico import tela_Historico
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
		self.stack5 = QtWidgets.QMainWindow()
		self.stack6 = QtWidgets.QMainWindow()
		self.stack7 = QtWidgets.QMainWindow()

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

		self.Tela_Deposito = Tela_Deposito()
		self.Tela_Deposito.setupUi(self.stack5)

		self.Tela_Saque = Tela_Saque()
		self.Tela_Saque.setupUi(self.stack6) 

		self.Tela_Historico = tela_Historico()
		self.Tela_Historico.setupUi(self.stack7)   

		self.QStack.addWidget(self.stack0)
		self.QStack.addWidget(self.stack1)
		self.QStack.addWidget(self.stack2)
		self.QStack.addWidget(self.stack3)
		self.QStack.addWidget(self.stack4)
		self.QStack.addWidget(self.stack5)
		self.QStack.addWidget(self.stack6)
		self.QStack.addWidget(self.stack7)

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

		self.Tela_Saque.pushButton_2.clicked.connect(self.botaoSacar2)
		self.Tela_Saque.pushButton.clicked.connect(self.voltar2)

		self.tela_transferir.pushButton.clicked.connect(self.voltar2)
		self.tela_transferir.pushButton_2.clicked.connect(self.botaoTranferir2)

		self.Tela_Historico.pushButton_2.clicked.connect(self.voltar2)

		self.Tela_Deposito.pushButton.clicked.connect(self.voltar2)
		self.Tela_Deposito.pushButton_2.clicked.connect(self.botaoDepositar2)

		p = Cliente(str(Cliente.cont), '1', '1', '1', 100.0)
		self.cad.cadastra(p)
		self.pessoa = None

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
		self.pessoa = self.cad.busca(numero, cpf)
		if (self.pessoa != None):
			self.menu()
			
		else:
			QMessageBox.information(None, 'POOII', 'Todos os valores devem ser preenchidos! ')

		return None

	def menu(self):
		self.QStack.setCurrentIndex(2)
		self.tela_usuario.pushButton_3.clicked.connect(self.botaoTranferir)
		self.tela_usuario.pushButton_5.clicked.connect(self.voltar)
		self.tela_usuario.pushButton.clicked.connect(self.botaoSacar)
		self.tela_usuario.pushButton_2.clicked.connect(self.botaoDepositar)
		self.tela_usuario.pushButton_4.clicked.connect(self.botaoHistorico)
		
		return None
		
	def botaoHistorico(self):
		texto = self.pessoa.historico.imprime()
		self.Tela_Historico.textEdit.setText(texto)
		self.QStack.setCurrentIndex(7)
	
	def botaoSacar(self):
		self.QStack.setCurrentIndex(6)
		self.Tela_Saque.lineEdit.setText('')
		self.Tela_Saque.lineEdit_2.setText(str(self.pessoa.saldo))

	def botaoSacar2(self):
		valor = self.Tela_Saque.lineEdit.text()
		self.pessoa.saca(valor)
		self.Tela_Saque.lineEdit_3.setText(str(self.pessoa.saldo))

	def botaoDepositar(self):
		self.Tela_Deposito.lineEdit.setText('')
		self.Tela_Deposito.lineEdit_3.setText('')
		self.Tela_Deposito.lineEdit_2.setText(str(self.pessoa.saldo))
		self.QStack.setCurrentIndex(5)
		valorDepositado = self.Tela_Deposito.lineEdit.text()

	def botaoDepositar2(self):
		deposito = float(self.Tela_Deposito.lineEdit.text())
		valorantigo = self.Tela_Deposito.lineEdit_2.text()
		self.pessoa.deposita(float(deposito))
		self.Tela_Deposito.lineEdit_3.setText(str(self.pessoa.saldo))

	def botaoTranferir(self):
		self.QStack.setCurrentIndex(3)
		self.tela_transferir.lineEdit.setText('')
		self.tela_transferir.lineEdit_2.setText('')
		self.tela_transferir.lineEdit_3.setText(str(self.pessoa.saldo)) 

	def botaoTranferir2(self):
		numero = self.tela_transferir.lineEdit.text()
		valor = self.tela_transferir.lineEdit_2.text()
		self.pessoa.transfere(numero, valor, self.cad._contas)
		self.tela_transferir.lineEdit_3.setText(str(self.pessoa.saldo))

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
