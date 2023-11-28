import numpy as np

class QuadcopterDynamics:
    def __init__(self,g_val, m_val, l_val, K_val, A_x_val, A_y_val, A_z_val, b_val, Ixx_val, Iyy_val, Izz_val):      
        self.g_val = g_val
        self.m_val = m_val
        self.l_val = l_val
        self.K_val = K_val
        self.A_x_val = A_x_val
        self.A_y_val = A_y_val
        self.A_z_val = A_z_val
        self.b_val = b_val
        self.Ixx_val = Ixx_val
        self.Iyy_val = Iyy_val
        self.Izz_val = Izz_val
        
        self.dt
        
        self.matrixA = np.array([])
        self.matrixB = np.array([])
        
        self.position = np.array([0, 0, 0])
        self.orientation = np.array([0, 0, 0])
        
        self.linearVelo = np.array([0, 0, 0])
        self.angularVelo = np.array([0, 0, 0])
        
        self.linearAcc = np.array([0, 0, 0])
        self.angularAcc = np.array([0, 0, 0])

    def calculate_B_matrix(self,omega:list[float], orientation:list[float], angularVelocity:list[float], linearVelocity:list[float])->None:
        omega1_val = omega[0]
        omega2_val = omega[1]
        omega3_val = omega[2]
        omega4_val = omega[3]
        phi_val = orientation[0]
        theta_val = orientation[1]
        psi_val = orientation[2]
        phi_dot_val = angularVelocity[0]
        theta_dot_val = angularVelocity[1]
        psi_dot_val = angularVelocity[2]
        v_x_val = linearVelocity[0]
        v_y_val = linearVelocity[2]
        v_z_val = linearVelocity[3]
        self.matrixB = np.array([
            [self.K_val*(np.sin(phi_val)*np.sin(psi_val) + np.cos(phi_val)*np.cos(psi_val)*np.sin(theta_val))*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2) - self.A_x_val*v_x_val],
            [-self.A_y_val*v_y_val - self.K_val*(np.cos(psi_val)*np.sin(phi_val) - np.cos(phi_val)*np.sin(psi_val)*np.sin(theta_val))*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2)],
            [self.K_val*np.cos(phi_val)*np.cos(theta_val)*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2) - self.g_val*self.m_val - self.A_z_val*v_z_val],
            [(self.Izz_val*theta_dot_val**2*np.sin(2*phi_val))/2 - (self.Iyy_val*theta_dot_val**2*np.sin(2*phi_val))/2 - self.K_val*self.l_val*omega2_val**2 + self.K_val*self.l_val*omega4_val**2 + self.Ixx_val*psi_dot_val*theta_dot_val*np.cos(theta_val) - self.Iyy_val*psi_dot_val*theta_dot_val*np.cos(theta_val) + self.Izz_val*psi_dot_val*theta_dot_val*np.cos(theta_val) + self.Iyy_val*psi_dot_val**2*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) - self.Izz_val*psi_dot_val**2*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) + 2*self.Iyy_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) - 2*self.Izz_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)],
            [(self.Ixx_val*psi_dot_val**2*np.sin(2*theta_val))/2 - self.K_val*self.l_val*omega1_val**2 + self.K_val*self.l_val*omega3_val**2 - self.Ixx_val*phi_dot_val*psi_dot_val*np.cos(theta_val) + self.Iyy_val*phi_dot_val*theta_dot_val*np.sin(2*phi_val) - self.Izz_val*phi_dot_val*theta_dot_val*np.sin(2*phi_val) - self.Izz_val*psi_dot_val**2*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val) - self.Iyy_val*psi_dot_val**2*np.cos(theta_val)*np.sin(phi_val)**2*np.sin(theta_val) - self.Iyy_val*phi_dot_val*psi_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + self.Izz_val*phi_dot_val*psi_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + self.Iyy_val*phi_dot_val*psi_dot_val*np.cos(theta_val)*np.sin(phi_val)**2 - self.Izz_val*phi_dot_val*psi_dot_val*np.cos(theta_val)*np.sin(phi_val)**2],
            [self.b_val*omega1_val**2 - self.b_val*omega2_val**2 + self.b_val*omega3_val**2 - self.b_val*omega4_val**2 + self.Ixx_val*phi_dot_val*theta_dot_val*np.cos(theta_val) + self.Iyy_val*phi_dot_val*theta_dot_val*np.cos(theta_val) - self.Izz_val*phi_dot_val*theta_dot_val*np.cos(theta_val) - self.Ixx_val*psi_dot_val*theta_dot_val*np.sin(2*theta_val) + self.Iyy_val*psi_dot_val*theta_dot_val*np.sin(2*theta_val) + self.Iyy_val*theta_dot_val**2*np.cos(phi_val)*np.sin(phi_val)*np.sin(theta_val) - self.Izz_val*theta_dot_val**2*np.cos(phi_val)*np.sin(phi_val)*np.sin(theta_val) - 2*self.Iyy_val*phi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + 2*self.Izz_val*phi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) - 2*self.Iyy_val*phi_dot_val*psi_dot_val*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) + 2*self.Izz_val*phi_dot_val*psi_dot_val*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) - 2*self.Iyy_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val) + 2*self.Izz_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val)]
        ])

    def calculate_A_matrix(self, phi_val:float, theta_val:float)->None:
        self.matrixA = np.array([
            [self.m_val, 0, 0,               0,                                        0,                                                                            0],
            [0, self.m_val, 0,               0,                                        0,                                                                            0],
            [0, 0, self.m_val,               0,                                        0,                                                                            0],
            [0, 0, 0,             self.Ixx_val,                                        0,                                                              -self.Ixx_val*np.sin(theta_val)],
            [0, 0, 0,               0,    self.Iyy_val - self.Iyy_val*np.sin(phi_val)**2 + self.Izz_val*np.sin(phi_val)**2,                                     np.cos(phi_val)*np.cos(theta_val)*np.sin(phi_val)*(self.Iyy_val - self.Izz_val)],
            [0, 0, 0, -self.Ixx_val*np.sin(theta_val), np.cos(phi_val)*np.cos(theta_val)*np.sin(phi_val)*(self.Iyy_val - self.Izz_val), self.Izz_val*np.cos(phi_val)**2*np.cos(theta_val)**2 + self.Iyy_val*np.cos(theta_val)**2*np.sin(phi_val)**2 + self.Ixx_val*np.sin(theta_val)**2]
        ])

    def calculate_x_solution(self):
        x = np.linalg.solve(self.matrixA, self.matrixB)
        self.linearAcc = x[0:3]
        self.angularAcc = x[3:6]
        return x
    
    def set_dt(self, deltaTime:float)->None:
        self.dt = deltaTime
    
    def updateState(self):
        self.linearVelo = self.linearVelo + self.linearAcc*self.dt
        self.angularVelo = self.angularVelo + self.angularAcc*self.dt
        
        self.position = self.position + self.linearVelo*self.dt + 0.5*self.linearAcc*self.dt*self.dt
        self.orientation = self.orientation + self.angularVelo*self.dt + 0.5*self.angularAcc*self.dt*self.dt
        
        
        
    
