
'''
Neste video é apresentado o modulo os
'''
import os
from datetime import datetime

print(dir(os))
#cria diretorio
try:
    os.mkdir('./dirprog10/')
except:
    pass


#cria arvore de diretorios
try:
    os.makedirs('./dirprog10/subdir/subsubdir')
except:
    pass
#lista os arquivos e diretorios dentro do diretorio
print(os.listdir())
#tamanho do arquivo
print(os.stat('prog03.py').st_size)
#data de criacao
print(datetime.fromtimestamp(os.stat('prog03.py').st_mtime))

# os.walk caminha em todos diretorios verificando os arquivo e pastas em todos eles


for dirpath, dirname,files in os.walk('./'):
    print(dirpath,dirname,files)