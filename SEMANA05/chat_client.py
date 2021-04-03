#!/usr/bin/python3
import socket 
import pickle 
import os
from datetime import datetime
import sys
from threading import Thread 

'''
msg 
	id
	msgid
	name
	hour
	message
	msgid
'''
commandos = ['delete','exit']
title = \
'''
Use \\n para quebra de linha
Use \\exit para sair 
Use \\delete ID para apagar uma mensage
'''
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class Chat:
	def __init__(self,name,host):
		self.handle = None
		self.name = name
		self.id = None
		self.msg = []
		self.msgId = 1
		self.host = host
		self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.run = True
	def connect(self):
		self.tcp.connect(self.host)
		def handle():
			while self.run:
				tamanho = self.tcp.recv(4)
				tamanho = int.from_bytes(tamanho, byteorder='big', signed=False)
				binaryMsg = self.tcp.recv(tamanho)
				msg = pickle.loads(binaryMsg)				
				if 'command' in msg:
					self.onReceiveCommand(msg['command'],msg['data'])
				else:
					self.msg.append(msg)
					self.printMsg()

		self.handle = Thread(target=handle,daemon=True)
		self.handle.start()


	def onReceiveCommand(self,command,data=None):
		if command == 'clear':
			self.msg = []
			return
		if command == 'id_set':
			self.id = data['id']
			self.printMsg()
			return
		if command == 'delete':
			for m in self.msg:
				if m['id'] == data['id'] and m['msgid'] == data['msgid']:
					m['message'] = '<---- mensagem  apagada ---->'
				self.printMsg()
				return
			
	def printMsg(self):
		cls()
		s = title
		for msg in self.msg:
			if msg['id'] == self.id:
				s = s + f'<-me- id({msg["msgid"]})'
			else:
				s = s + f">-{msg['name']}"
			s= s + f"[{msg['hour']}]{{\n"
			s = s+ msg['message']+'\n}'
		print(s+'\n>>',end='')
		
	def checkMsg(self,msg):
		if msg.startswith('\\'):
			if not msg.startswith('\\\\'):
				data = msg[1:].split(' ')
				if  data[0] in commandos:
					if data[0] == 'delete':
						if len(data) >=2:
							try:
								data = {'command':data[0],'data':{'id':self.id,'msgid':int(data[1])}}
								self.send(data)
								return
							except Exception as e:
								pass
					if data[0] == 'exit':
						self.run = False
				return 
		self.sendMsg(msg)

	def sendMsg(self,msg):
		msg = msg.split('\n')
		msg ='\t'+'\n\t'.join(msg)
		msg = {'id':self.id,'hour':datetime.now().strftime("%H:%M:%S"),'name':self.name,'message':msg,'msgid':self.msgId}
		self.msgId += 1
		#self.msg.append(msg)
		self.send(msg)


	def send(self,msg):
		toSend = pickle.dumps(msg)
		self.tcp.send(len(toSend).to_bytes(length=4, byteorder='big', signed=False))
		self.tcp.send(toSend)


if len(sys.argv)!= 4:
	print('''Esperado os seguintes argumentos
	IP PORT NAME''')
	sys.exit(-1)


ip = sys.argv[1]
port = int(sys.argv[2])
name  = sys.argv[3]

me  = Chat(name,(ip,port))
me.connect()
print('conectando ...')
while me.run:
	entrada = input()
	me.checkMsg(entrada)