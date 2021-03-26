
'''
Neste video é apresentado como escrever em arquivos
'''
# abrindo como escrita existe alguns modos
# w a r , escrita apagando td, escrita em seguida, leitura, e se colocar b na frente é modo binario


with open('prog011.txt','w') as f:
    print('escrevendo no arquivo',file=f)
    f.write('tambem escrevo assim')

with open('prog011.txt','r') as f:
    print(f.read())


# o with chama o metodo close automaticamente
