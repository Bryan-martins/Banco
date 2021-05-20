import socket
from Multitela import *
import sys

ip = 'localhost'
port = 8000
addr = (ip,port)
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(addr)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	show_main = Main(cliente_socket)
	app.exec_()
	cliente_socket.close()
	sys.exit()
    