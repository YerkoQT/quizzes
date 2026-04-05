import numpy as np
import matplotlib.pyplot as plt
#tiempo de simulacion
h=1
T=200
tc=80			
#parametros(constantes)
m0=1000
μ=10
ve=1000
g=9.81
β=5
#creacion de vectores
t=np.arange(0,T+h,h)
m=np.where(t<tc, m0-μ*t, m0-μ*tc)
n=len(t)
v=np.zeros(n)
x=np.zeros(n)
#condiciones iniciales
x[0]=0
v[0]=0
x[1]=x[0]+v[0]*h
v[1]=v[0]+h*(ve*μ-m[0]*g-β*v[0])/m[0]
#verlet
for i in range(1, n-1):
	x[i+1]=2*x[i]-x[i-1]+h**2*(ve*μ-m[i]*g-β*v[i])/m[i] if t[i]<= tc else 2*x[i]-x[i-1]+h**2*(-m[i]*g-β*v[i])/m[i]
	v[i+1]=v[i-1]+2*h*(ve*μ-m[i]*g-β*v[i])/m[i] if t[i]<= tc else v[i]+h*(-m[i]*g-β*v[i])/m[i]
#grafica
fig, axs =plt.subplots(1, 2, figsize=(10, 6))
fig.suptitle(f"Diferencias Finitas 2do Orden  |  m₀={m0} kg  μ={μ} kg/s  vₑ={ve} m/s  β={β}",fontweight='bold')
#posicion
axs[0].plot(t, x)
axs[0].set(title='Posicion x(t)', xlabel='Tiempo [s]', ylabel='Altura [m]')
axs[0].axvline(x=tc, color='r', linestyle='--')
#velocidad
axs[1].plot(t, v)
axs[1].set(title='Velocidad x(t)', xlabel='Tiempo [s]', ylabel='Velocidad [m/s]')
axs[1].axvline(x=tc, color='r', linestyle='--')
#guardar y mostrar
plt.savefig('verlet.png')
plt.show()