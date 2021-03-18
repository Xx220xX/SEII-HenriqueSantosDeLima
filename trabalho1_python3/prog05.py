estudante = {'name':'Henrique','age':20,'couses':['Math','Math2']}
estudante['phone'] ='123'
print(estudante.get('phone','not found'))

del estudante['phone']
print(estudante.get('phone','not found'))
print(estudante.items())
for key,value in estudante.items():
    print(key,value)
'''
Neste video é apresentado os dicionarios
'''