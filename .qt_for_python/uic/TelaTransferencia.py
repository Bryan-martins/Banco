# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Val\Documents\Sistema de Informação 2018.1\4ª Período\POO II\Lista 06 - Interface III\BANCOPOO\TelaTransferencia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.frame.setStyleSheet("background-color: rgb(236, 236, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 160, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 380, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.pushButtonTransferenciaVoltar = QtWidgets.QPushButton(self.frame)
        self.pushButtonTransferenciaVoltar.setGeometry(QtCore.QRect(380, 450, 75, 23))
        self.pushButtonTransferenciaVoltar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButtonTransferenciaVoltar.setObjectName("pushButtonTransferenciaVoltar")
        self.pushButtonTransferenciaConfirmar = QtWidgets.QPushButton(self.frame)
        self.pushButtonTransferenciaConfirmar.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.pushButtonTransferenciaConfirmar.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButtonTransferenciaConfirmar.setObjectName("pushButtonTransferenciaConfirmar")
        self.lineEditTransferenciaNumConta = QtWidgets.QLineEdit(self.frame)
        self.lineEditTransferenciaNumConta.setGeometry(QtCore.QRect(350, 170, 181, 20))
        self.lineEditTransferenciaNumConta.setStyleSheet("")
        self.lineEditTransferenciaNumConta.setObjectName("lineEditTransferenciaNumConta")
        self.lineEditTransferenciaNovoSaldo = QtWidgets.QLineEdit(self.frame)
        self.lineEditTransferenciaNovoSaldo.setGeometry(QtCore.QRect(350, 380, 181, 20))
        self.lineEditTransferenciaNovoSaldo.setStyleSheet("color: rgb(0, 0, 0);")
        self.lineEditTransferenciaNovoSaldo.setObjectName("lineEditTransferenciaNovoSaldo")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 801, 80))
        self.frame_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(280, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(190, 170, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(280, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.lineEditTransferenciaValor = QtWidgets.QLineEdit(self.frame)
        self.lineEditTransferenciaValor.setGeometry(QtCore.QRect(350, 210, 181, 20))
        self.lineEditTransferenciaValor.setStyleSheet("")
        self.lineEditTransferenciaValor.setObjectName("lineEditTransferenciaValor")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Saldo: "))
        self.pushButtonTransferenciaVoltar.setText(_translate("MainWindow", "Voltar"))
        self.pushButtonTransferenciaConfirmar.setText(_translate("MainWindow", "Confirmar"))
        self.label.setText(_translate("MainWindow", "B&V Bank"))
        self.label_4.setText(_translate("MainWindow", "Numero da conta:"))
        self.label_5.setText(_translate("MainWindow", "Valor:"))
