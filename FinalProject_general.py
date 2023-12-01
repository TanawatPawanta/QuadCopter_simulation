from QuadcopterDynamics import QuadcopterDynamics
import time
import numpy as np
from simtest import Quadcopter3DVisualization, QuadcopterController


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


# [x y z ]
position = [0, 0, 0]
linear_velo = [0, 0, 0]
# [phi theta psi]
orientation = [0, 0, 0]
angular_velo = [0, 0, 0]
# [m1 m2 m3 m4]
omega = [0, 0, 0 ,0]

myTimer = time.time()
print("Start time : ",myTimer)
dt = 0.01
timeStamp = time.time() + dt
clk = 0
step = 0
quadcopter.calculate_A_matrix(phi_val=orientation[0], theta_val=orientation[1])
quadcopter.calculate_B_matrix(omega=omega, orientation=orientation, angularVelocity=angular_velo, linearVelocity=linear_velo)
acc = quadcopter.calculate_x_solution()
while True:
    if(time.time()-timeStamp >= 0):
        if step >= 100:
            print("Start time : ",myTimer)
            print("Stop time : ", time.time())
            break
        else:
            step = step+1
            quadcopter.calculate_A_matrix(phi_val=orientation[0], theta_val=orientation[1])
            quadcopter.calculate_B_matrix(omega=omega, orientation=orientation, angularVelocity=angular_velo, linearVelocity=linear_velo)
            acc = quadcopter.calculate_x_solution()
            linear_velo = linear_velo + acc[0:3]*dt
            timeStamp = time.time() + dt