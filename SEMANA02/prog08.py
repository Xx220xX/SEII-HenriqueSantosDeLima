def func1():
    print('from func1')

# com parametros
def func2(prm0,prm1):
    print('from func2')
    print(prm0,prm1)

# com parametro incializado
def func3(parm0=0):
    print('from func3')
    print('valor recebido foi',parm0)

# com argumentos variaveis

def func4(*args):
    print('from func4')
    print('Os parametos recebidos foram {')
    for a in args:
        print(a,end=' ')
    print('\n}')
# com argumentos e chaves variaveis

def func5(nome, *args,**kwargs):
    print('from func5')
    print('seu nome',nome)
    print(args)
    print(kwargs)
# com retorno
def func6(a:int,b:int)->int:
    print("from func6")
    return a+b

# com descricao
def  func7(a,b):
    '''
    essa funcao faz a multiplicacao de a e b
    :return: a*b
    '''
    print("from func7")
    return a*b


func1()
func2(1,2)
func3()
func3(8)
func4(1,2,3,6,4)
func5('henrique','arg1',2,idade=20)
func6(2,5)
func7(2,5)

# help(func7)
'''
Neste video é apresentado as funcoes
'''