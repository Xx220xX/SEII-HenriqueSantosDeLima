
'''
modulo datetime
'''

import datetime,pytz

hoje =  datetime.date.today()
print(hoje)
print(datetime.date.weekday(hoje))
print(datetime.date.isoweekday(hoje))

tdelta = datetime.timedelta(hours=24)
print(hoje+tdelta)

diaAleatorio = datetime.date(2016,9,24)
tmp = (hoje-diaAleatorio)
print(tmp.days)
dt  =  datetime.datetime(2021,3,12,10,30,20,tzinfo=pytz.UTC)
# mostra os atributos de dt
print(dir(dt))


#data a partir de string

dtst= '24 de July de 2021'
dt = datetime.datetime.strptime(dtst,'%d de %B de %Y')
print(dt)

