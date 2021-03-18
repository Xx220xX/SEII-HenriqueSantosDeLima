
'''
variaveis locais e globais

'''


#variaveis globais podem ser acesadas por qualquer escopo
for a in range(2):
    x = 'global {}'.format(a)
def func():
    # o escopo dessa fucao é outro portanto atribuir x aqui nao afetara o x global
    # mas é possivel ler o valor de x
    for b in range(3):
        x = 'global {}'.format(b)
    def inner():
        #funcao pertencente ao escopo de func
        # esta tem acesso ao x de func
        print(globals())
        for c in range(3):
            x = 'global {}'.format(c)
        print(x)
        print(a,b,b)
    inner()
    print(x)
    print(a,b)
func()
print(x)
print(a)

#para ver as variaveis global vc usa print(globals())
# para locais print(locals())
# existe a flag global para ter acesso as varfiaveis globais
def func2():
    def inner():
        global x
        x = 'inner que manda aqui'
    inner()
def func3():
    def inner():
        x = 'inner 2 que manda aqui'
    inner()
print(x)
func2()
print(x)

func3()
print(x)