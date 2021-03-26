
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# grafico
x = list(range(5))
y = list(range(0, 9, 2))
# plt.plot(x, y,label='2x',color='red',linewidth=2,marker='.',markersize=10,markeredgecolor='blue')
#  modo curto
plt.figure(figsize=(5,3),dpi=300)
plt.plot(x, y,'b.:',label='2x')

x2 = np.arange(0,4.5,0.5)
plt.plot(x2,x2**2,'r',label='x²')
plt.title('grafico', fontdict={'fontname': 'Consolas', 'fontsize': 20})
plt.xlabel('x')
plt.ylabel('y')
plt.yticks(y + [10])
plt.xticks(x)
plt.legend()
plt.savefig('grafi.png',dpi=300)
plt.show()
