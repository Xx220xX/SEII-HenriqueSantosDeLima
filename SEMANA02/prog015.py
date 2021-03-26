
'''
modulo csv  e html
'''

import csv

html = ''
nomes = []

with open('patrons.csv','r') as csvf:
    csvR = csv.DictReader(csvf)
    next(csvR)#pular primeira linha do csv
    for line in csvR:
        if line['FirstName'] == 'No Reward':break
        nomes.append(f"{line['FirstName']} {line['LastName']}")

html  += f'<p> Existem atualmente {len(nomes)} contribuidores públicos. Obrigado!</p>'
html += '\n<ul>'
for nome in nomes:
    html += f'\n\t<li>{nome}</li>'
html += '\n<ul>'
print(html)