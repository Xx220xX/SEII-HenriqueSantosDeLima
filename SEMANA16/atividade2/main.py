import numpy as np
import math
import matplotlib.pyplot as plt
from control.matlab import *
def generateRK4(h,A,B):
	print('AB',A,B,sep='\n')
	def x_dot(t,x,u):
		xkp1 = A @ x + B @ u
		return xkp1

	def rk4(tk,xk,uk):
		xk = xk.reshape([2,1])
		uk = uk.reshape([1,1])

		k1 = x_dot(tk,xk,uk)
		k2 = x_dot(tk+h/2.0,xk+h*k1/2.0,uk)
		k3 = x_dot(tk+h/2.0,xk+h*k2/2.0,uk)
		k4 = x_dot(tk+h,xk+h*k3,uk)
		xkp1 = xk + (h/6.0)*(k1 + 2.0*k2 + 2.0*k3 + k4)
		return xkp1.reshape([2,])
	return rk4
def gerarConpensador(G,Mp,ts=2):
	zeta = np.sqrt(np.log(Mp)**2/(np.pi**2+np.log(Mp)**2))
	wn = 4/(zeta*ts)

	#  polo dominante
	polo = [zeta*wn,wn*np.sqrt(1-zeta*zeta)]
	poloComplex = -polo[0]+polo[1]*1j
	

	theta = math.atan2(polo[1],polo[0])
	phi = np.pi/2 - theta
	beta = (np.pi - theta)/2
	gamma = theta+beta-phi/2-np.pi/2
	a = polo[0] + polo[1]*np.tan(gamma)
	b = polo[0] + polo[1]*np.tan(gamma+phi)

	# compensador sem ganho
	C_k = tf([1,a],[1,b])
	#ganho
	K = abs(1/(evalfr(C_k,poloComplex)*evalfr(G,poloComplex)))
	C = K*C_k
	return tf(C)
def generateEqdif(a,b,y0=0,x0=0):
	a = list(a)
	print('a',a)
	print('b',b)
	
	a0 = a.pop(0)
	b = np.array(b)/a0
	a = np.array(a)/a0
	print('a',a)
	print('b',b)
	
	y_ = list((np.zeros([1,len(a)]) + y0)[0])
	x_ = list((np.zeros([1,len(b)]) + x0)[0])
	def eqdf(x):
		x_.pop()
		x_.insert(0,x)
		y = np.array(x_)*b - np.array(y_)*a
		y_.insert(0,y)
		y_.pop()
		
		return y
	return eqdf
if __name__ == '__main__':
	# Função de transferencia
	G = tf([9],[1,2,9])
	# print(G)
	# plt.figure()
	# rlist, klist = rlocus(G)
	# sisotool(G)
	# plt.show()
	
	#  Avanço de fase
	C = gerarConpensador(G,0.1,2)
	print(C)
	T = feedback(C*G,1)
	print(T)
	t = np.arange(0,3,1e-3)
	u = t*0+1;
	y,x,*k = lsim(T,u,t)
	plt.figure('a')
	plt.plot(x,y)
	plt.title('Resposta ao degrau do sistema em malha fechada')
	plt.grid()

	

	# Item b
	Ts = 0.01
	Cz = c2d(C,Ts,method = 'zoh')
	print(Cz)
	
	Gss = tf2ss(G)
	
	h = 1e-4
	maxT = 3
	mult = math.floor(Ts/h)
	rk4 = generateRK4(h,Gss.A,Gss.B)
	t = np.arange(0,maxT,h)
	tu = np.arange(0,maxT,Ts)

	x = np.zeros([2,len(t)])
	u = np.zeros([len(tu)])
	r = np.ones([len(t)-1])
	y = np.zeros([len(t)-1])

	
	eqdf = generateEqdif(Cz.den[0][0],Cz.num[0][0])
	p = 0

	for k in range(len(t)-1):
		y[k] = Gss.C @ x[:,k]
		if k%mult == 0 :
			ek = r[k] - y[k]
			u[p] = eqdf(ek)
			p+= 1
		x[:,k+1] = rk4(t[k],x[:,k],u[p-1])

	plt.figure('Simulacao')
	plt.subplot(211)
	plt.plot(t,x[0,:])
	plt.plot(t,x[1,:])
	plt.legend(['1','2'])
	
	plt.figure('s2')
	plt.plot(tu,u)


	
	
	# ekm1 = 0
	# ukm1 = 0
	# p = 0
	# for k in range(kmax):
	# 	y[k] = Gss.C @ x[:,k]
	# 	if (k%mult)==0:
	# 		ek = r[k]-y[k]
	# 		u[p] = k2_u * ukm1 + K * (ek - k1_u * ekm1)
	# 		ekm1 = ek
	# 		ukm1 = u[p]
	# 		p += 1
	# 	x[:,k+1] = rk4(t[k],h,x[:,k],u[p-1])
	
	# plt.figure('1')
	# plt.subplot(2,1,1)
	# plt.plot(t,x[0,:])
	# plt.ylabel('x_1')
	# plt.subplot(2,1,2)
	# plt.plot(t,x[1,:])
	# plt.ylabel('x_2')

	# plt.figure('2')
	# plt.plot(t[0:-1],y,label='y_1')
	# plt.plot(t[0:-1],r,label='r_1')
	# plt.ylabel('y_1')

	# plt.figure('3')
	# plt.plot(tu[0:len(u)],u,label='u_1')
	# plt.ylabel('u_1')
	plt.show()
