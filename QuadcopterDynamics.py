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
        
        self.dt = 0
        
        self.matrixA = np.array([])
        self.matrixB = np.array([])
        
        self.position = np.array([0, 0, 0]).astype(float)
        self.orientation = np.array([0, 0, 0]).astype(float)
        self.position_minus = np.array([0, 0, 0]).astype(float)
        self.orientation_minus = np.array([0, 0, 0]).astype(float)
        
        self.linearVelo = np.array([0, 0, 0]).astype(float)
        self.angularVelo = np.array([0, 0, 0]).astype(float)
        self.linearVelo_minus = np.array([0, 0, 0]).astype(float)
        self.angularVelo_minus = np.array([0, 0, 0]).astype(float)
        
        self.linearAcc = np.zeros(3,).astype(float)
        self.angularAcc = np.zeros(3,).astype(float)
        
    def calculate_A_matrix(self, phi_val:float, theta_val:float)->None:
        self.matrixA = np.array([])
        self.matrixA = np.array([
            [self.m_val, 0, 0,               0,                                        0,                                                                            0],
            [0, self.m_val, 0,               0,                                        0,                                                                            0],
            [0, 0, self.m_val,               0,                                        0,                                                                            0],
            [0, 0, 0,             self.Ixx_val,                                        0,                                                              -self.Ixx_val*np.sin(theta_val)],
            [0, 0, 0,               0,    self.Iyy_val - self.Iyy_val*np.sin(phi_val)**2 + self.Izz_val*np.sin(phi_val)**2,                                     np.cos(phi_val)*np.cos(theta_val)*np.sin(phi_val)*(self.Iyy_val - self.Izz_val)],
            [0, 0, 0, -self.Ixx_val*np.sin(theta_val), np.cos(phi_val)*np.cos(theta_val)*np.sin(phi_val)*(self.Iyy_val - self.Izz_val), self.Izz_val*np.cos(phi_val)**2*np.cos(theta_val)**2 + self.Iyy_val*np.cos(theta_val)**2*np.sin(phi_val)**2 + self.Ixx_val*np.sin(theta_val)**2]
        ])
        
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
        v_y_val = linearVelocity[1]
        v_z_val = linearVelocity[2]
        self.matrixB = np.array([])
        self.matrixB = np.array([
            [self.K_val*(np.sin(phi_val)*np.sin(psi_val) + np.cos(phi_val)*np.cos(psi_val)*np.sin(theta_val))*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2) - self.A_x_val*v_x_val],
            [-self.A_y_val*v_y_val - self.K_val*(np.cos(psi_val)*np.sin(phi_val) - np.cos(phi_val)*np.sin(psi_val)*np.sin(theta_val))*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2)],
            [self.K_val*np.cos(phi_val)*np.cos(theta_val)*(omega1_val**2 + omega2_val**2 + omega3_val**2 + omega4_val**2) - self.g_val*self.m_val - self.A_z_val*v_z_val],
            [(self.Izz_val*theta_dot_val**2*np.sin(2*phi_val))/2 - (self.Iyy_val*theta_dot_val**2*np.sin(2*phi_val))/2 - self.K_val*self.l_val*omega2_val**2 + self.K_val*self.l_val*omega4_val**2 + self.Ixx_val*psi_dot_val*theta_dot_val*np.cos(theta_val) - self.Iyy_val*psi_dot_val*theta_dot_val*np.cos(theta_val) + self.Izz_val*psi_dot_val*theta_dot_val*np.cos(theta_val) + self.Iyy_val*psi_dot_val**2*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) - self.Izz_val*psi_dot_val**2*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) + 2*self.Iyy_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) - 2*self.Izz_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)],
            [(self.Ixx_val*psi_dot_val**2*np.sin(2*theta_val))/2 - self.K_val*self.l_val*omega1_val**2 + self.K_val*self.l_val*omega3_val**2 - self.Ixx_val*phi_dot_val*psi_dot_val*np.cos(theta_val) + self.Iyy_val*phi_dot_val*theta_dot_val*np.sin(2*phi_val) - self.Izz_val*phi_dot_val*theta_dot_val*np.sin(2*phi_val) - self.Izz_val*psi_dot_val**2*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val) - self.Iyy_val*psi_dot_val**2*np.cos(theta_val)*np.sin(phi_val)**2*np.sin(theta_val) - self.Iyy_val*phi_dot_val*psi_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + self.Izz_val*phi_dot_val*psi_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + self.Iyy_val*phi_dot_val*psi_dot_val*np.cos(theta_val)*np.sin(phi_val)**2 - self.Izz_val*phi_dot_val*psi_dot_val*np.cos(theta_val)*np.sin(phi_val)**2],
            [self.b_val*omega1_val**2 - self.b_val*omega2_val**2 + self.b_val*omega3_val**2 - self.b_val*omega4_val**2 + self.Ixx_val*phi_dot_val*theta_dot_val*np.cos(theta_val) + self.Iyy_val*phi_dot_val*theta_dot_val*np.cos(theta_val) - self.Izz_val*phi_dot_val*theta_dot_val*np.cos(theta_val) - self.Ixx_val*psi_dot_val*theta_dot_val*np.sin(2*theta_val) + self.Iyy_val*psi_dot_val*theta_dot_val*np.sin(2*theta_val) + self.Iyy_val*theta_dot_val**2*np.cos(phi_val)*np.sin(phi_val)*np.sin(theta_val) - self.Izz_val*theta_dot_val**2*np.cos(phi_val)*np.sin(phi_val)*np.sin(theta_val) - 2*self.Iyy_val*phi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) + 2*self.Izz_val*phi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val) - 2*self.Iyy_val*phi_dot_val*psi_dot_val*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) + 2*self.Izz_val*phi_dot_val*psi_dot_val*np.cos(phi_val)*np.cos(theta_val)**2*np.sin(phi_val) - 2*self.Iyy_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val) + 2*self.Izz_val*psi_dot_val*theta_dot_val*np.cos(phi_val)**2*np.cos(theta_val)*np.sin(theta_val)]
        ])


    def calculate_x_solution(self):
        x = np.linalg.solve(self.matrixA, self.matrixB)
        self.linearAcc = x[0:3]
        self.angularAcc = x[3:6]
        return x
    
    def set_dt(self, deltaTime:float)->None:
        self.dt = deltaTime
        
    def Rot_zyx(self, phi, theta, psi):
        R_x = np.array([[1, 0, 0],
                        [0, np.cos(phi), -np.sin(phi)],
                        [0, np.sin(phi), np.cos(phi)]
                        ])

        R_y = np.array([[np.cos(theta), 0, np.sin(theta)],
                        [0, 1, 0],
                        [-np.sin(theta), 0, np.cos(theta)]
                        ])

        R_z = np.array([[np.cos(psi), -np.sin(psi), 0],
                        [np.sin(psi), np.cos(psi), 0],
                        [0, 0, 1]
                        ])

        R = np.dot(R_z, np.dot(R_y, R_x))
        return R
    
    def updateState(self):
        # print("Updating...")
        deltasPos = np.zeros(3,)
        deltasOrien = np.zeros(3,)
        for i in range(3):
            # update current state
            self.linearVelo[i] = self.linearVelo_minus[i] + (self.linearAcc[i]*self.dt)
            self.angularVelo[i] = self.angularVelo_minus[i] + self.angularAcc[i]*self.dt
            self.position[i] = self.position_minus[i] + self.linearVelo[i]*self.dt + 0.5*self.linearAcc[i]*self.dt*self.dt
            self.orientation[i] = self.orientation_minus[i] + self.angularVelo[i]*self.dt + 0.5*self.angularAcc[i]*self.dt*self.dt
            deltasPos[i] = self.linearVelo[i]*self.dt + 0.5*self.linearAcc[i]*self.dt*self.dt
            deltasOrien[i] = self.angularVelo[i]*self.dt + 0.5*self.angularAcc[i]*self.dt*self.dt
            # update n-1 state
            self.linearVelo_minus[i] = self.linearVelo[i]
            self.angularVelo_minus[i] = self.angularVelo[i]
            self.position_minus[i] = self.position[i]
            self.orientation_minus[i] = self.orientation[i]
        return np.concatenate((deltasOrien,deltasPos),axis=0)
    
    def dynamicDebugger(self):
        # print("Linear prpoties")
        print("Linear accelaration : ",self.linearAcc.T)
        # print("Linear velocity : ",self.linearVelo)
        # print("Position : ",self.position) 

        # print("Angular prpoties")
        print("Angular accelaration : ",self.angularAcc.T)
        # print("Angular velocity : ",self.angularVelo)
        # print("Orientation : ",self.orientation)   

        
    
