#!usr/bin/python3

# gerar as sequencias 

n = 20
y=[1]
for i in range(1,n):
	y.append(y[-1]+2)

print(y)