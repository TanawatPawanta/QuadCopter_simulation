import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from pyplot3d.uav import Uav
from pyplot3d.utils import ypr_to_R

def update_plot(i, x, R):
    uav_plot.draw_at(x[:, i], R[:, :, i])       #draw on matplotlib
    
    lim = 2

    xmin, xmax = -lim, lim
    ymin, ymax = -lim, lim
    zmin, zmax = -lim, lim
    
    ax.set_xlim([xmin, xmax])                   #set matplotlib window
    ax.set_ylim([ymax, ymin])
    ax.set_zlim([zmax, zmin])

fig = plt.figure()                              #init plot
ax = fig.add_subplot(111, projection='3d')

arm_length = 0.24  # in meters
uav_plot = Uav(ax, arm_length)                  #init uav

steps = 1000
t_end = 300

#input xyz
x = np.zeros((3, steps))

x[0, :] = np.arange(0, t_end, t_end / steps)            # x
x[1, :] = np.arange(0, t_end, t_end / steps) * 2        # y
x[2, :] = np.arange(0, t_end, t_end / steps) * -2       # z

#input ypr
R = np.zeros((3, 3, steps))

for i in range(steps):
    ypr = np.array([i*5, 0, 0])                         #yaw pitch roll
    R[:, :, i] = ypr_to_R(ypr, degrees=True)            #convert ypr to Rotation matrix

ani = animation.FuncAnimation(fig, update_plot, frames=30, fargs=(x, R,))   #make animation
ani.save('animation.gif', writer='pillow', fps=30)                          #save animation