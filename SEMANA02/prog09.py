
'''
Neste video é apresentado ois modulos
onde posso importar funcoes de outros modulos
'''
# importando um modulo criado por mim

import prog08 as functions
functions.func1()

# importando funcoes especificas

from prog08 import  func7
func7(1,2)

# importando td do modulo para este

from prog08 import *
func2(9,8)