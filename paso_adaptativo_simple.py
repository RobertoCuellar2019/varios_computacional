import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# parámetros para el sistema considerado
g = 9.8
l = 0.1
#condiciones iniciales
theta_ini = 179*np.pi/180 # posición inicial del péndulo
theta_dot_ini = 0 # velocidad inicial del péndulo
condiciones_iniciales =np.array([theta_ini, theta_dot_ini]) # arreglo de condiciones iniciales
delta = 1e-5 # preción deseada
tiempo_inicial = 0
tiempo_final = 10
h_prima = [] # Arreglo donde se guardan los pasos dados
tiempo_array = [] # Arreglo donde se guarda el eje temporal
# sistema de ecuaciones diferenciales .... en este caso... péndulo simple

def sistema_(x,t,g,l):
    # x[0] equivale a theta, x[1] equivale a theta punto
    dtheta = x[1]
    domega = -(g/l)*np.sin(x[0])
    return np.array([dtheta, domega])
# integraciones para h y 2h 
def integraciones (t1,t2, condiciones_iniciales, g,l,sistema_):
        integracion1 = odeint(sistema_, condiciones_iniciales, t1, args = (g,l)) # integración para h (t1 trae 3 elementos)
        integracion2 = odeint(sistema_, condiciones_iniciales, t2, args = (g,l)) # integración para 2h (t2 trae 2 elementos)
        result = np.zeros([3], dtype = np.float64) # arreglo donde se guardarán los resultados 
        x1, x2 =  integracion1[:,0][2], integracion2[:,0][1] # valor de theta(t+2h) para las dos integraciones
        x3 = integracion2[:,1][1] # velocidad en el punto
        result[0] = x1
        result[1] = x2
        result[2] = x3
        return result
# solución ideal
tiempo_ideal = np.linspace(tiempo_inicial, tiempo_final, 100)
integracion_ideal = odeint(sistema_, condiciones_iniciales, tiempo_ideal, args = (g,l)) # integración para h (t1 trae 3 elementos)


h = 0.1 #tamaño del paso random inicial
h_ini = h # se guarda este valor
tiempo_array.append(tiempo_inicial) # se rellena la primera posición del arreglo temporal
theta_array = [] # arreglo para el valor de theta con el tiempo
theta_array.append(theta_ini) # se rellena la primera posición del arreglo de theta
theta_dot_array = []
theta_dot_array.append(theta_dot_ini)
while (tiempo_inicial <= tiempo_final): # calculo adaptativo de theta y tiempo
    t1 = np.array([tiempo_inicial, tiempo_inicial+h, tiempo_inicial+2*h]) # arreglo para paso h
    t2 = np.array([tiempo_inicial, tiempo_inicial+2*h]) # arreglo para paso 2h
    resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se obtienen los  valores de theta(t+2h) para ambos métodos
    x1 = resultados[0] # theta(t+2h) paso h
    x2 = resultados[1] # theta(t+2h) paso 2h
    #error = abs(x1-x2)/30
    rho = 30*h*delta/abs(x1-x2)
    rho = round(rho,1)
    rho = int(rho)
    print('Rho inicial = ', rho,'----------------------------------------------------------------------------------')
#    quit()
    if rho > 1 :
        #y = 1
        while(rho > 1):
            h = h+(h_ini/1000)
            #h = round(h,5)
            t1 = np.array([tiempo_inicial, tiempo_inicial+h, tiempo_inicial+2*h]) # arreglo para paso h
            t2 = np.array([tiempo_inicial, tiempo_inicial+2*h]) # arreglo para paso 2h
            resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se obtienen los  valores de theta(t+2h) para ambos métodos
            x1 = resultados[0] # theta(t+2h) paso h
            x2 = resultados[1] # theta(t+2h) paso 2h
            rho = 30*h*delta/abs(x1-x2)
            rho = round(rho,0)
            rho = int(rho)
            print('rho actual = ',rho,'h = ',h)
            #y += 1
        t2 = np.array([tiempo_inicial, tiempo_inicial+h]) # se utiliza el valor de h establecido
        resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se calculan los resultados para t2
        x2 = resultados[1] # valor te theta(t+h)
        x3 = resultados[2] # velocidad angular en theta(t+h)
        theta_array.append(x2) # se guarda el nuevo valor de theta en el arreglo
        theta_dot_array.append(x3) # se guarda el nuevo valor de la velocidad en el arreglo
        tiempo_inicial += h # se incrementa el valor del tiempo inicial
        tiempo_array.append(tiempo_inicial) # se guarda en la última posición
        # se deben actualizar ahora las condiciones iniciales de integración para la próxima iteración
        condiciones_iniciales =np.array([theta_array[-1], theta_dot_array[-1]]) # arreglo de condiciones iniciales
        print('tiempos = ', tiempo_array,'theta = ',theta_array, 'omega = ', theta_dot_array)
    else :
        if rho < 1 :
            #y = 1
            while(rho < 1):
                h = h-(h_ini/1000)
                #h = round(h,5)
                t1 = np.array([tiempo_inicial, tiempo_inicial+h, tiempo_inicial+2*h]) # arreglo para paso h
                t2 = np.array([tiempo_inicial, tiempo_inicial+2*h]) # arreglo para paso 2h
                resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se obtienen los  valores de theta(t+2h) para ambos métodos
                x1 = resultados[0] # theta(t+2h) paso h
                x2 = resultados[1] # theta(t+2h) paso 2h
                rho = 30*h*delta/abs(x1-x2)
                rho = round(rho,0)
                rho = int(rho)
  #          print('rho actual = ',rho,'h = ',h)
            #y += 1
            t2 = np.array([tiempo_inicial, tiempo_inicial+h]) # se utiliza el valor de h establecido
            resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se calculan los resultados para t2
            x2 = resultados[1] # valor te theta(t+h)
            x3 = resultados[2] # velocidad angular en theta(t+h)
            theta_array.append(x2) # se guarda el nuevo valor de theta en el arreglo
            theta_dot_array.append(x3) # se guarda el nuevo valor de la velocidad en el arreglo
            tiempo_inicial += h # se incrementa el valor del tiempo inicial
            tiempo_array.append(tiempo_inicial) # se guarda en la última posición
        # se deben actualizar ahora las condiciones iniciales de integración para la próxima iteración
            condiciones_iniciales =np.array([theta_array[-1], theta_dot_array[-1]]) # arreglo de condiciones iniciales
            print('tiempos = ', tiempo_array,'theta = ',theta_array, 'omega = ', theta_dot_array)
        else:
            t2 = np.array([tiempo_inicial, tiempo_inicial+h]) # se utiliza el valor de h establecido
            resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se calculan los resultados para t2
            x2 = resultados[1] # valor te theta(t+h)
            x3 = resultados[2] # velocidad angular en theta(t+h)
            theta_array.append(x2) # se guarda el nuevo valor de theta en el arreglo
            theta_dot_array.append(x3) # se guarda el nuevo valor de la velocidad en el arreglo
            tiempo_inicial += h # se incrementa el valor del tiempo inicial
            tiempo_array.append(tiempo_inicial) # se guarda en la última posición
            # se deben actualizar ahora las condiciones iniciales de integración para la próxima iteración
            condiciones_iniciales =np.array([theta_array[-1], theta_dot_array[-1]]) # arreglo de condiciones iniciales
            print('rho =1  tiempos = ', tiempo_array,'theta = ',theta_array, 'omega = ', theta_dot_array)

            

   #     quit()

  #  if rho == 1:
  #      t2 = np.array([tiempo_inicial, tiempo_inicial+h]) # se utiliza el valor de h establecido
  #      resultados = np.array(integraciones(t1,t2,condiciones_iniciales, g, l, sistema_)) # se calculan los resultados para t2
  #      x2 = resultados[1] # valor te theta(t+h)
  #      x3 = resultados[2] # velocidad angular en theta(t+h)
  #      theta_array.append(x2) # se guarda el nuevo valor de theta en el arreglo
  #      theta_dot_array.append(x3) # se guarda el nuevo valor de la velocidad en el arreglo
  #      tiempo_inicial += h # se incrementa el valor del tiempo inicial
  #      tiempo_array.append(tiempo_inicial) # se guarda en la última posición
  #      # se deben actualizar ahora las condiciones iniciales de integración para la próxima iteración
  #      condiciones_iniciales =np.array([theta_array[-1], theta_dot_array[-1]]) # arreglo de condiciones iniciales
  #      print('rho =1  tiempos = ', tiempo_array,'theta = ',theta_array, 'omega = ', theta_dot_array)

        # quit()
    #quit()
print('Tiempo = ',tiempo_ideal ,'ideal = ',integracion_ideal[:,0])
plt.scatter(tiempo_array, theta_array, color = 'red')
plt.scatter(tiempo_ideal, integracion_ideal[:,0], color = 'blue')
plt.show()









