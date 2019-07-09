import numpy as np
from math import * # con esto se garantiza que eval pueda recibir "cualquier" funcion 


class euler_normal:
    
    def euler_1er(self, y_prima, lim_sup, lim_inf, h, yo):
        
        N = int(((lim_sup-lim_inf)/h)+1)
        x_v = np.linspace(lim_inf, lim_sup, N)
        y_v = np.zeros([N],dtype=float)
        y_v[0] = yo
        for i in range(N-1):
            x = x_v[i]
            y = y_v[i]
            valor_func = float(eval(y_prima))
            y_v[i+1] = y_v[i]+ h*valor_func
        return(x_v, y_v)
    
    def euler_2do(self, v_prima, lim_sup, lim_inf, h, yo, vo):
        
        N = int(((lim_sup-lim_inf)/h)+1)
        x_v = np.linspace(lim_inf, lim_sup, N)
        v_v = np.zeros([N],dtype=float)
        y_v = np.zeros([N],dtype=float) 
        v_v[0] = vo
        y_v[0] = yo
        for i in range(N-1):
            x = x_v[i]
            y = y_v[i]
            v = v_v[i]
            valor_func = float(eval(v_prima))
            v_v[i+1] = v_v[i] + h*valor_func
            y_v[i+1] = y_v[i] + h*v_v[i]
        return(x_v,y_v,v_v)

class euler_mejorado:
    def euler_1er_m(self, y_prima, lim_sup, lim_inf, h, yo):
        
       
        N = int(((lim_sup-lim_inf)/h)+1)
        x_v = np.linspace(lim_inf, lim_sup, N)
        y_v = np.zeros([N],dtype=float)
        y_v[0] = yo
        for i in range(N-1):
            x = x_v[i]
            y = y_v[i]
            valor_func_1 = float(eval(y_prima))
            y_p= y_v[i] + h*valor_func_1
            y = y_p            
            x = x_v[i+1]
            valor_func_2 = float(eval(y_prima))
            y_v[i+1] = y_v[i]+ h*0.5*(valor_func_2+valor_func_1)        
        return(x_v, y_v)
        

    def euler_2do_m(self, v_prima, lim_sup, lim_inf, h, yo, vo):                
        N = int(((lim_sup-lim_inf)/h)+1)
        x_v = np.linspace(lim_inf, lim_sup, N)
        v_v = np.zeros([N],dtype=float)
        y_v = np.zeros([N],dtype=float)
        v_v[0] = vo
        y_v[0] = yo
        for i in range(N-1):
            x = x_v[i]
            y = y_v[i]
            v = v_v[i]
            valor_func_1 = float(eval(v_prima))
            v_p = v_v[i] + h*valor_func_1
            v = v_p
            x = x_v[i+1]
            y = y_v[i]
            valor_func_2 = float(eval(v_prima))
            v_v[i+1] = v_v[i]+ h*0.5*(valor_func_2+valor_func_1)   
            y_v[i+1] = y_v[i] + h*(v_v[i])
        return(x_v,y_v,v_v)

        
        
        
    def euler_2do_cromer(self, v_prima, lim_sup, lim_inf, h, yo, vo):                
        N = int(((lim_sup-lim_inf)/h)+1)
        x_v = np.linspace(lim_inf, lim_sup, N)
        v_v = np.zeros([N],dtype=float)
        y_v = np.zeros([N],dtype=float)
        v_v[0] = vo
        y_v[0] = yo
        for i in range(N-1):
            x = x_v[i]
            y = y_v[i]
            v = v_v[i]
            valor_func_1 = float(eval(v_prima))
            v_p = v_v[i] + h*valor_func_1
            v = v_p
            x = x_v[i+1]
            y = y_v[i]
            valor_func_2 = float(eval(v_prima))
            v_v[i+1] = v_v[i]+ h*0.5*(valor_func_2+valor_func_1)   
            y_v[i+1] = y_v[i] + h*(v_v[i+1])
        return(x_v,y_v,v_v)