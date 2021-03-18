
'''
ordenacao de lista

'''

# metodos sort e sorted
#sorted cria uma nova lista
#sort organiza a propria lista


l = [1,4,3,2,10,65,3]

l2 = sorted(l)
print(l2)
print(l)#l nao for ordenada

# l.sort()
# print(l)# l foi ordenada


t = tuple(l)
# tuiples nao possui o metodo sort
print(sorted(t))

# pode ser passado uma funcao para atribuir um valor ordenavel a um objeto, util para organizar dicionarios

d = []

for i in range(len(l)):
    d.append({'name':f'pessoa{i}','age':l[i]})

# dd = sorted(d)

dd2 = sorted(d,key=lambda a:a['age'])
for pessoa in dd2:
    nome , idade = pessoa.values()
    print(nome,idade)