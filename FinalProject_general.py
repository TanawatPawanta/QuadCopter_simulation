from QuadcopterDynamics import QuadcopterDynamics
from simtest import Quadcopter3DVisualization, QuadcopterController
import time
import numpy as np
import math

# quadcopter parameters
# gravity
g_val = 9.81
# mass 
m_val = 0.468
# distance between propeller
l_val = 0.225
# lift constant
K_val = 2.980*1e-6
# air resistant coeff
A_x_val = 0.0
A_y_val = 0.0
A_z_val = 0.0
# drag constant
b_val = 1.14*1e-7
# innertia
Ixx_val = 4.856*1e-3
Iyy_val = 4.856*1e-3
Izz_val = 8.801*1e-3

# Create an instance of QuadcopterDynamics
quadcopter = QuadcopterDynamics(g_val, m_val, l_val, K_val, A_x_val, A_y_val, A_z_val, b_val, Ixx_val, Iyy_val, Izz_val)
quadcopter_visualization = Quadcopter3DVisualization()
quadcopter_controller = QuadcopterController(quadcopter_visualization)
# [x y z ]
# [phi theta psi]
# [m1 m2 m3 m4]
om = 1.075
spd = om*math.sqrt(1/K_val)
print("spd : ",spd)
dspd = 0.05*spd
# #spin about z-axis and move +z
# omega = [spd-(0.5*dspd), spd+(0.5*dspd), spd-(0.5*dspd), spd+(0.5*dspd)]
# #spin about x-axis
omega = [spd, spd-(0.5*dspd), spd, spd]
print("omega", omega)
myTimer = time.time()
print("Start time : ",myTimer)
dt = 0.01
quadcopter.set_dt(dt)

clk = 0
step = 0
timeStamp = time.time() + dt
deltas = np.zeros(6,)
print("timeStamp : ", timeStamp)
while True:
    if(time.time()-timeStamp >= 0):
        print("========trick=======")
        quadcopter_controller.update_quadcopter_and_plot(deltas=deltas)
        if step < 0:
            print("Start time : ",myTimer)
            print("Stop time : ", time.time())
            break
        else:
            step = step+1
            print("Step number : ",step)     
            quadcopter.calculate_A_matrix(phi_val=quadcopter.orientation[0], theta_val=quadcopter.orientation[1])
            quadcopter.calculate_B_matrix(omega=omega, orientation=quadcopter.orientation, angularVelocity=quadcopter.angularVelo, linearVelocity=quadcopter.linearVelo)
            acc = quadcopter.calculate_x_solution()
            deltas = quadcopter.updateState()          
            quadcopter.dynamicDebugger()
        timeStamp = time.time() + dt    