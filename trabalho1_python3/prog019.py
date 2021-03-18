
'''
Excessoes em python

'''
try :
    #funcao que pode gerar erro
    pass
except Exception:
    # tratar erro
    pass
finally:
    #executar apos o try ou o except, sera executado
    pass

try:
    # raise Exception('um erro aconteceu')
    print('Td certo')
except Exception as e:
    print(e)
finally:
    print('finally')

# criar exceçao

class MyException(Exception):

    def __init__(self) -> None:
        super().__init__('aconteceu um erro')


try:
    raise MyException()
except MyException as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('finally')
