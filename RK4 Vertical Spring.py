from manim import *

frame_rate = 60
config.frame_rate = frame_rate
#Acceleration to gravity
grav = 9.81
#Initial Displacement
A = 1.00
#Spring Constant
k = 10.00
#Damping Coefficient
b = 1.00
#Mass of system
m= 1.00
#StepLength
h = 1/frame_rate
#Number of itterations for RK4
n = 600

def f(t,y,v):
    return -k/m*y - grav

def g(t,y,v):
    return v

#RK4 Subprograms
def RK4_Algo(t_n, y_n, v_n, step_len):

    k1v = f(t_n,y_n,v_n)
    k1x = g(t_n,y_n,v_n)

    k2v = f(t_n + step_len/2 ,y_n + step_len/2*k1x ,v_n + step_len/2*k1v)
    k2x = g(t_n + step_len/2 ,y_n + step_len/2*k1x ,v_n + step_len/2*k1v)

    k3v = f(t_n + step_len/2 ,y_n + step_len/2*k2x ,v_n + step_len/2*k2v)
    k3x = g(t_n + step_len/2 ,y_n + step_len/2*k2x ,v_n + step_len/2*k2v)

    k4v = f(t_n + step_len,y_n+step_len*k3x,v_n+step_len*k3v)
    k4x = g(t_n + step_len,y_n+step_len*k3x,v_n+step_len*k3v)

    
    t_n1 = t_n + step_len
    y_n1 = y_n + step_len/6 * (k1x + 2*k2x + 2*k3x + k4x)
    v_n1 = v_n + step_len/6 * (k1v + 2*k2v + 2*k3v + k4v)

    return t_n1, y_n1, v_n1

#Itteration Calculator
def RK4_Itteration(Itterations,Step_Len,t_null, y_null,v_null):
    
    t_values = []
    y_values = []
    v_values = []

    t_i, y_i, v_i = t_null, y_null, v_null
    
    t_values.append(t_null)
    y_values.append(y_null)
    v_values.append(v_null)


    for i in range(Itterations):
        
        t_i , y_i, v_i = RK4_Algo(t_i, y_i, v_i, Step_Len)
        t_values.append(t_i)
        y_values.append(y_i)
        v_values.append(v_i)
        
    return t_values, y_values, v_values


t_values , y_values, v_values = RK4_Itteration(Itterations = n, Step_Len = h, t_null = 0, y_null = A, v_null = 0)



#Moving the mass
class Animation(Scene):
    def construct(self):
        time_general = ValueTracker(0)

        def y():
            return y_values[int(time_general.get_value()/h)]
        
        Mass = always_redraw(lambda:  Circle(radius = 0.5, color= WHITE).move_to([0,y(),0]) )
        self.add(Mass)

        Spring = always_redraw(lambda: ParametricFunction(lambda t: np.array([0.25 * np.sin(20*2*np.pi*t/(y()-2.5)), t+3, 0]), t_range = [y()-2.5,0]))
        self.add(Spring)

        self.play(time_general.animate.set_value(n*h), run_time = n*h, rate_func = linear)

        


        











        
        
            
            