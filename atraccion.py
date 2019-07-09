# una partícula orbitando objeto masivo en forma de cilindro justo en su centro de masa, el objeto cilíndrico se puede aproximar a una linea asumiendo que su radio es mucho menor que su longitud, por lo que se usa densidad de masa lineal, constante en este caso
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# Todo en sistema internacional
# parámetros para el sistema considerado
m1  = 10 # 
l = 2. # 
G = 1 # constante gravitacional en algún universo

#condiciones iniciales
x_ini = 1
y_ini = 0
xdot_ini = 0
ydot_ini = 1
condiciones_iniciales =np.array([x_ini, y_ini, xdot_ini, ydot_ini])
tiempo_inicial = 0
tiempo_final = 10
N = 1000
tiempo = np.linspace(tiempo_inicial, tiempo_final, N) # vector de tiempo
def sistema_(x,t,m1,l,G):
    # x[0] equivale a x, x[1] xdot, x[2] = y , x[3] = ydot
    dx = x[1]
    dy = x[3]
    dvx =-(G*m1*x[0])/((((x[0]**2)+(x[2]**2))**1)*((x[0]**2)+(x[2]**2)+((l/2)**2))**0.5)
    dvy =-(G*m1*x[2])/((((x[0]**2)+(x[2]**2))**1)*((x[0]**2)+(x[2]**2)+((l/2)**2))**0.5)
   
    return np.array([dx, dvx,  dy, dvy])
# solución del sistema de ecuaciones acopladas
integracion, infodict= odeint(sistema_, condiciones_iniciales, tiempo,args = (m1,l,G),full_output=True)
infodict['message']  # se muestra un mensaje del status de la integración

plt.plot(integracion[:,0],integracion[:,2])
plt.title('Órbita')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
#plt.plot(tiempo,integracion[:,2])
#plt.grid(True)
#plt.show()

