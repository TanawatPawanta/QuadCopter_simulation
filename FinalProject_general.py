from QuadcopterDynamics import QuadcopterDynamics
from simtest import Quadcopter3DVisualization, QuadcopterController
from SlidebarClass import MotorSpeedSliders
import time
import numpy as np
import math

g_val = 9.81 
m_val = 0.468
l_val = 0.225
K_val = 2.980*1e-6
A_x_val = 0.0
A_y_val = 0.0
A_z_val = 0.0
b_val = 1.14*1e-7
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


step = 0
timeStamp = time.time() + dt
deltas = np.zeros(6,)
state = "init_state"
while True:
    if(time.time()-timeStamp >= 0):
        print("========trick=======")
        print("State :",state)
        # quadcopter visualization
        if step >= 500:
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
                    if(motor_speed_sliders.enter_press == True):
                        omega = motor_speed_sliders.get_speed()
                        motor_speed_sliders.close_window()
                        state = "VisualizatioConsrtruct_state"
                        del motor_speed_sliders
                case "VisualizatioConsrtruct_state":
                    
                    quadcopter_visualization = Quadcopter3DVisualization()
                    quadcopter_controller = QuadcopterController(quadcopter_visualization)
                    state = "simulation_state"
                case "simulation_state":
                    quadcopter_controller.update_quadcopter_and_plot(deltas=deltas)
                    step = step+1
                    print("Step number : ",step)     
                    quadcopter.calculate_A_matrix(phi_val=quadcopter.orientation[0], theta_val=quadcopter.orientation[1])
                    quadcopter.calculate_B_matrix(omega=omega, orientation=quadcopter.orientation, angularVelocity=quadcopter.angularVelo, linearVelocity=quadcopter.linearVelo)
                    acc = quadcopter.calculate_x_solution()
                    deltas = quadcopter.updateState()     
                    print("Deltas : ",deltas)     
                    quadcopter.dynamicDebugger()              
        timeStamp = time.time() + dt    