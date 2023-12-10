from QuadcopterDynamics import QuadcopterDynamics
from simtest import Quadcopter3DVisualization, QuadcopterController
from Visualization_v2 import update_plot
from pyplot3d.utils import ypr_to_R
from Input_GUI import MotorSpeedSliders
import time
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation
from pyplot3d.uav import Uav

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

# del motor_speed_sliders
quadcopter = QuadcopterDynamics(g_val, m_val, l_val, K_val, A_x_val, A_y_val, A_z_val, b_val, Ixx_val, Iyy_val, Izz_val)



# [x y z ]
# [phi theta psi]
# [m1 m2 m3 m4]
om = 1.075
spd = om*math.sqrt(1/K_val)
dspd = 0.05*spd
# #spin about z-axis and move +z
omega = [spd-(0.5*dspd), spd+(0.5*dspd), spd-(0.5*dspd), spd+(0.5*dspd)]
# #spin about x-axis
# omega = [spd, spd-dspd, spd, spd]
# #spin about y-axis
# omega = [spd-dspd, spd, spd, spd]
# omega = [620.6108 , 620.6108, 620.6108-10, 620.6108] 

print("omega", omega)
myTimer = time.time()
print("Start time : ",myTimer)
dt = 0.01
quadcopter.set_dt(dt)

sim_time = 100
X = np.zeros((3,sim_time))    #store position
R = np.zeros((3, 3, sim_time))  #store orientation
step = 0
timeStamp = time.time() + dt
deltas = np.zeros(6,)
state = "init_state"
while True:
    if(time.time()-timeStamp >= 0):
        print("========trick=======")
        print("State :",state)
        # quadcopter visualization
        if step >= sim_time-1:
            print("Start time : ",myTimer)
            print("Stop time : ", time.time())
            break
        else:
            match state:
                case "init_state":
                    state = "MotorSpeedSlidersConstruct_state"
                case "MotorSpeedSlidersConstruct_state":
                    motor_speed_sliders = MotorSpeedSliders()
                    state = "input_state"
                case "input_state":
                    motor_speed_sliders.run()
                    if(motor_speed_sliders.startSim_press == True):
                        omega = motor_speed_sliders.get_speed()
                        motor_speed_sliders.close_window()
                        state = "simulation_state"
                        del motor_speed_sliders
                case "simulation_state":
                    step = step+1
                    print("Step number : ",step)     
                    quadcopter.calculate_A_matrix(phi_val=quadcopter.orientation[0], theta_val=quadcopter.orientation[1])
                    quadcopter.calculate_B_matrix(omega=omega, orientation=quadcopter.orientation, angularVelocity=quadcopter.angularVelo, linearVelocity=quadcopter.linearVelo)
                    acc = quadcopter.calculate_x_solution()
                    pos = quadcopter.updateState()       
                    quadcopter.dynamicDebugger()    
                    X[:,step] = pos[3:6].T 
                    R[:, :, step] = ypr_to_R(pos[0:3], degrees=True)         
        timeStamp = time.time() + dt    

fig = plt.figure()                              #init plot
ax = fig.add_subplot(111, projection='3d')

arm_length = l_val  # in meters
uav_plot = Uav(ax, arm_length)                  #init uav

ani = animation.FuncAnimation(fig, update_plot, frames=30, fargs=(X, R,))   #make animation
ani.save('animation.gif', writer='pillow', fps=30)                          #save animation