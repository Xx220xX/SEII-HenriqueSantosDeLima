#!/usr/bin/python3
import sys
import socket
if len(sys.argv)!= 4:
	print('''Argumentos esperados
	 IP porta file_name''')
	sys.exit(-1)

HOST = sys.argv[1]         	   # Endereco IP do Servidor
port =  int(sys.argv[2])           # Porta que o Servidor esta
file_name = sys.argv[3]



# CRIAR SERVIDOR 
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, port)
tcp_client.connect(orig)


# receber dados
datalen = tcp_client.recv(4)
datalen = int.from_bytes(datalen, byteorder='big', signed=False)
data = tcp_client.recv(datalen)

# salvar
try:
	open(file_name,'wb').write(data)
except Exception as e:
	print(e)
	sys.exit(-1)

tcp_client.close()
