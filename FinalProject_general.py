from QuadcopterDynamics import QuadcopterDynamics
from simtest import Quadcopter3DVisualization, QuadcopterController
import time
import numpy as np

g_val = 9.81
m_val = 1.0
l_val = 0.5
K_val = 0.01
A_x_val = 0.02
A_y_val = 0.03
A_z_val = 0.04
b_val = 0.05
Ixx_val = 0.1
Iyy_val = 0.2
Izz_val = 0.3

# Create an instance of QuadcopterDynamics
quadcopter = QuadcopterDynamics(g_val, m_val, l_val, K_val, A_x_val, A_y_val, A_z_val, b_val, Ixx_val, Iyy_val, Izz_val)
# quadcopter_visualization = Quadcopter3DVisualization()
# quadcopter_controller = QuadcopterController(quadcopter_visualization)
# [x y z ]
# [phi theta psi]
# [m1 m2 m3 m4]
omega = [100, 100, 100 ,100]

myTimer = time.time()
print("Start time : ",myTimer)
dt = 0.01
quadcopter.set_dt(dt)

clk = 0
step = 0
timeStamp = time.time() + dt
print("timeStamp : ", timeStamp)
while True:
    if(time.time()-timeStamp >= 0):
        print("========trick=======")
        # quadcopter_controller.update_quadcopter_and_plot(position=quadcopter.position,orientation=quadcopter.orientation)
        if step >= 100:
            print("Start time : ",myTimer)
            print("Stop time : ", time.time())
            break
        else:
            step = step+1
            print("Step number : ",step)
            quadcopter.dynamicDebugger()
            quadcopter.calculate_A_matrix(phi_val=quadcopter.orientation[0], theta_val=quadcopter.orientation[1])
            quadcopter.calculate_B_matrix(omega=omega, orientation=quadcopter.orientation, angularVelocity=quadcopter.angularVelo, linearVelocity=quadcopter.linearVelo)
            acc = quadcopter.calculate_x_solution()
            quadcopter.updateState()           
        timeStamp = time.time() + dt    