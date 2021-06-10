import numpy as np
import matplotlib.pyplot as plt
from control.matlab import *

def x_dot(t,x,u):
    A = np.array( [[-2., -9.],\
                  [ 1.,  0.]])
    B = np.array([[1.],\
                 [0.]])
    xkp1 = A @ x + B @ u
    return xkp1

def rk4(tk,h,xk,uk):
    xk = xk.reshape([2,1])
    uk = uk.reshape([1,1])

    k1 = x_dot(tk,xk,uk)
    k2 = x_dot(tk+h/2.0,xk+h*k1/2.0,uk)
    k3 = x_dot(tk+h/2.0,xk+h*k2/2.0,uk)
    k4 = x_dot(tk+h,xk+h*k3,uk)

    xkp1 = xk + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)

    return xkp1.reshape([2,])

if __name__ == '__main__':
    # Função de transferencia
    G = tf([9],[1,2,9])
    Gss = tf2ss(G)
    print(Gss)
    Ts = 0.01
    h = 1e-4
    maxT = 10
    mult = Ts/h
    t = np.arange(0,maxT,h)
    tu = np.arange(0,maxT,Ts)

    x = np.zeros([2,len(t)])
    u = np.zeros([len(tu)])
    r = np.ones([len(t)-1])
    y = np.zeros([len(t)-1])

    kmax = len(t)-1

    #PID
    Kp=8
    Ki=1
    Kd=0.7

    ek_1 = 0
    uk_1 = 0
    p = 0
    for k in range(kmax):
        y[k] = Gss.C @ x[:,k]
        if (k%mult)==0:
            ek = r[k]-y[k]
            u[p] = Kp * ek + uk_1 + (Ki*Ts/2)*(ek + ek_1) + (2*Kd/Ts)*(ek - ek_1) - uk_1
            ek_1 = ek
            uk_1 = u[p]
            p += 1
        x[:,k+1] = rk4(t[k],h,x[:,k],u[p-1])
    

    plt.figure('2')
    plt.plot(t[0:-1],y,label='y_1')
    plt.plot(t[0:-1],r,label='r_1')
    plt.grid()
    plt.ylabel('y_1')

    plt.show()