
'''
modulo csv
'''

import csv
with open('names.csv','r') as csvf:
    csvR = csv.DictReader(csvf)
    with open('novosNomes.csv','w') as ncsvf:
        csvW = csv.DictWriter(ncsvf,fieldnames=['Nome','Sobrenome'],delimiter='\t')
        csvW.writeheader()
        for l  in csvR:
            del l['email']
            csvW.writerow(l)
