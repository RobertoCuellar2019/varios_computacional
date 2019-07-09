# péndulo simple sin aproximacón para pequeños ángulos, se verifica que la dinámica del movimiento no es lineal

from vpython import *
import numpy as np
scene.range = .15 # se define la dimensión de la escena 
from scipy.integrate import odeint
# parámetros para el sistema considerado
g = 9.8
l = 0.1
#condiciones iniciales
theta_ini = 179*np.pi/180 
theta_dot_ini = 0 
condiciones_iniciales =np.array([theta_ini, theta_dot_ini])
tiempo_inicial = 0 
tiempo_final = 10
#delta_t = .01 # intervalo temporal
N = 1000
tiempo = np.linspace(tiempo_inicial, tiempo_final, N) # vector de tiempo
def sistema_(x,t,g,l):
    # x[0] equivale a x, x[1] equivale a y
    dtheta = x[1]
    domega = -(g/l)*np.sin(x[0])
    return np.array([dtheta, domega])
# solución del sistema de ecuaciones acopladas
integracion, infodict= odeint(sistema_, condiciones_iniciales, tiempo,args = (g,l),full_output=True)
infodict['message']  # se muestra un mensaje del status de la integración
masa = sphere(pos = vec(l*np.sin(theta_ini),-l*np.cos(theta_ini),0),radius = 0.01, color = color.red, make_trail = True) 
rod = cylinder(pos=vector(0,0,0), axis=vector(l*np.sin(theta_ini),-l*np.cos(theta_ini),0), radius=.001)
theta = integracion[:,0]
for i in range(len(theta)):
	rate(10) # fotogramas por segundo
	masa.pos = vec(l*np.sin(theta[i]),-l*np.cos(theta[i]),0)
	rod.axis = vec(l*np.sin(theta[i]),-l*np.cos(theta[i]),0)

