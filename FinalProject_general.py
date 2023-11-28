# import numpy as np

# # Example values
# omega1_val = 1.0
# omega2_val = 2.0
# omega3_val = 3.0
# omega4_val = 4.0
# phi_val = 0.1
# theta_val = 0.2
# psi_val = 0.3
# phi_dot_val = 0.01
# theta_dot_val = 0.02
# psi_dot_val = 0.03
# v_x_val = 0.1
# v_y_val = 0.2
# v_z_val = 0.3

# g_val = 9.81
# m_val = 1.0
# l_val = 0.5
# K_val = 0.01
# A_x_val = 0.02
# A_y_val = 0.03
# A_z_val = 0.04
# b_val = 0.05
# Ixx_val = 0.1
# Iyy_val = 0.2
# Izz_val = 0.3

# # MATLAB B matrix
# B_matrix = np.array([
#     [K_val*(np.sin(phi_val)*np.sin(psi_val) + np.cos(phi_val)*np.cos(psi_val)*np.sin(theta_val))*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2) - A_x_val*v_x_val],
#     [-A_y_val*v_y_val - K_val*(np.cos(psi_val)*np.sin(phi_val) - np.cos(phi_val)*np.sin(psi_val)*np.sin(theta_val))*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2)],
#     [K_val*np.cos(phi_val)*np.cos(theta_val)*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2) - g_val*m_val - A_z_val*v_z_val],
#     [(Izz_val*theta_dot_val**2*np.sin(2*phi_val))/2 - (Iyy_val*theta_dot_val**2*np.sin(2*phi_val))/2 - K_val*l_val*omega2_val**2 + K_val*l_val*omega4_val**2 + Ixx_val*psi_dot_val*theta_dot_val*np.cos(theta_val) - Iyy_val*psi_dot_val*theta_dot_val*np.cos(theta_val) + Izz_val*psi_dot_val*theta_dot_val*np.cos(theta_val) + Iyy_val*psi_dot_val**2*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) - Izz_val*psi_dot_val**2*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) + 2*Iyy_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) - 2*Izz_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)],
#     [(Ixx_val*psi_dot_val**2*np.sin(2*theta_val))/2 - K_val*l_val*omega1_val**2 + K_val*l_val*omega3_val**2 - Ixx_val*phi_dot_val*psi_dot_val*np.cos(theta_val) + Iyy_val*phi_dot_val*theta_dot_val*np.sin(2*phi_val) - Izz_val*phi_dot_val*theta_dot_val*np.sin(2*phi_val) - Izz_val*psi_dot_val**2*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val) - Iyy_val*psi_dot_val**2*np.cos(theta_val)*np.sin(phi_val)**2*np.sin(theta_val) - Iyy_val*phi_dot_val*psi_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + Izz_val*phi_dot_val*psi_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + Iyy_val*phi_dot_val*psi_dot_val*np.cos(theta_val)*np.sin(phi_val)**2 - Izz_val*phi_dot_val*psi_dot_val*np.cos(theta_val)*np.sin(phi_val)**2],
#     [b_val*omega1_val**2 - b_val*omega2_val**2 + b_val*omega3_val**2 - b_val*omega4_val**2 + Ixx_val*phi_dot_val*theta_dot_val*np.cos(theta_val) + Iyy_val*phi_dot_val*theta_dot_val*np.cos(theta_val) - Izz_val*phi_dot_val*theta_dot_val*np.cos(theta_val) - Ixx_val*psi_dot_val*theta_dot_val*np.sin(2*theta_val) + Iyy_val*psi_dot_val*theta_dot_val*np.sin(2*theta_val) + Iyy_val*theta_dot_val**2*np.cos(phi_val)*np.sin(phi_val)*np.sin(theta_val) - Izz_val*theta_dot_val**2*np.cos(phi_val)*np.sin(phi_val)*np.sin(theta_val) - 2*Iyy_val*phi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + 2*Izz_val*phi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) - 2*Iyy_val*phi_dot_val*psi_dot_val*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) + 2*Izz_val*phi_dot_val*psi_dot_val*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) - 2*Iyy_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val) + 2*Izz_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val)]
# ])

# # Define the matrix A
# A_matrix = np.array([
#     [m_val, 0, 0,               0,                                        0,                                                                            0],
#     [0, m_val, 0,               0,                                        0,                                                                            0],
#     [0, 0, m_val,               0,                                        0,                                                                            0],
#     [0, 0, 0,             Ixx_val,                                        0,                                                              -Ixx_val*np.sin(theta_val)],
#     [0, 0, 0,               0,    Iyy_val - Iyy_val*np.sin(phi_val)**2 + Izz_val*np.sin(phi_val)**2,                                     np.cos(phi_val)*np.cos(theta_val)*np.sin(phi_val)*(Iyy_val - Izz_val)],
#     [0, 0, 0, -Ixx_val*np.sin(theta_val), np.cos(phi_val)*np.cos(theta_val)*np.sin(phi_val)*(Iyy_val - Izz_val), Izz_val*np.cos(phi_val)**2*np.cos(theta_val)**2 + Iyy_val*np.cos(theta_val)**2*np.sin(phi_val)**2 + Ixx_val*np.sin(theta_val)**2]
# ])

# # Print the matrix A
# print("Matrix A:")
# print(A_matrix)
# # Print the Matrix B
# print("Matrix B:")
# print(B_matrix)

# x_solution = np.linalg.solve(A_matrix, B_matrix)
# # Print the solution
# print("Solution for x:")
# print(x_solution)

from QuadcopterDynamics import QuadcopterDynamics
import time
import numpy as np

# Example values
# omega1_val = 1.0
# omega2_val = 2.0
# omega3_val = 3.0
# omega4_val = 4.0

# phi_val = 0.1
# theta_val = 0.2
# psi_val = 0.3

# phi_dot_val = 0.01
# theta_dot_val = 0.02
# psi_dot_val = 0.03

# v_x_val = 0.1
# v_y_val = 0.2
# v_z_val = 0.3

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


# # Calculate and print the matrices
# quadcopter.calculate_A_matrix(0.1, 0.2)
# quadcopter.calculate_B_matrix(1.0, 2.0, 3.0, 4.0, 0.1, 0.2, 0.3, 0.01, 0.02, 0.03, 0.1, 0.2, 0.3)
# # Solve for x
# x_solution = quadcopter.calculate_x_solution()

# print("Matrix A:")
# print(quadcopter.matrixA)

# print("Matrix B:")
# print(quadcopter.matrixB)


# print("Solution for x:")
# print(x_solution)
# print(type(x_solution))

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