
'''
renomeando multiplos arquivos
'''
import os,shutil
try:
    os.mkdir('./prog013')
except:pass
# os.chdir('./prog013')
print(os.getcwd())# diretorio atual
# printar todos arquivos do diretorio

for f in os.listdir():
    if not os.path.isfile(f):continue
    if f =='.DS_store':continue
    fileSplit = f.split('.',1)
    filename , file_ext  = fileSplit
    if not '0' in filename: continue
    fTitulo , fn = filename.split('0',1)
    fTitulo = fTitulo.strip()
    fn = fn.strip()
    fn.zfill(2)
    shutil.copy(f,f'./prog013/{fn}{fTitulo}.{file_ext}')
    print(fTitulo,fn)


