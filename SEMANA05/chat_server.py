#!/usr/bin/python3
import sys
import socket
import pickle
from threading import Thread,Lock


if len(sys.argv)!= 2:
	print('''Argumentos esperados
	porta ''')
	sys.exit(-1)

HOST = ''              		   # Endereco IP do Servidor
port =  int(sys.argv[1])            # Porta que o Servidor esta
id_n = 1
lk = Lock()
# CRIAR SERVIDOR 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, port)
tcp.bind(orig)
tcp.listen()

clients = {}
def iteractionWithClient(con,client):
	global id_n
	global tcp
	global clients 
	print('client ',client)
	with lk:
		mid = id_n
		clients[mid]= con
		command = {'command':'id_set','data':{'id':mid}}
		id_n = id_n+1
		msg = pickle.dumps(command)
		sbyts = len(msg).to_bytes(length=4, byteorder='big', signed=False)
		con.send(sbyts)
		con.send(msg)
	try:
		while True:
			size = con.recv(4)
			data = con.recv(int.from_bytes(size, byteorder='big', signed=False))
			with lk:
				for  i ,c in clients.items():
					try:
						c.send(size)
						c.send(data)
					except Exception as e:
						print('falha')
						print(e)
	except Exception as e:
		print(e)
	with lk:
		del clients[mid]



def acceptClients():
	while True:
		con,client = tcp.accept()
		Thread(target=iteractionWithClient,args=(con,client)).start()

Thread(target=acceptClients,daemon=True).start()


while True:
	x = input()
	if x == 'exit':
		break
	print('Para sair digite: "exit"')
  
    

