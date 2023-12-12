# Quadcopter Simulation
> This project aims to visualize a Quadcopter's motion (roll, pitch, yaw, and hover) in 3D space by adjusting the speed of four motors using Python. The project consists of three main parts: motor speed adjustment window, dynamic calculation, and 3D visualization. Special thanks to [this MATLAB script](https://youtu.be/4hlQ2pf842U?si=a1AfHnj8r89j6BRX) for finding the Quadcopter's equation of motion.
# Table of Contents
 - [**Installation**](#installation)
 - [**Component**](#component)
 - [**User Guide**](#userguide)
 - [**Demos & Result**](#demosnresult)
 - [**Conclusion**](#conclusion)
 - [**Future plan**](#futureplans)
 - [**Reference**](#reference)
 
## Installation <a name="installation"></a>

### Pygame

> 1. Open Visual Studio Code.
> 2. Go to the terminal or open a new terminal.
> 3. Copy and paste the following command:
>    ```bash
>    pip install pygame
>    ```
> 4. Press Enter and wait for the download to complete.

### OpenGL

> 1. Open Visual Studio Code.
> 2. Go to the terminal or open a new terminal.
> 3. Copy and paste the following command:
>    ```bash
>    pip install PyOpenGL
>    pip install PyOpenGL_accelerate
>    ```
> 4. Press Enter and wait for the download to complete.

### Numpy

> 1. Open Visual Studio Code.
> 2. Go to the terminal or open a new terminal.
> 3. Copy and paste the following command:
>    ```bash
>    pip install numpy
>    ```
> 4. Press Enter and wait for the download to complete.
   
# Component <a name="component"></a>
### Motor Slider
> Description
> 
### Dynamic Calculation
> >
### 3D Visualization
> The visualization part involves drawing the Quadcopter on the screen and updating its position based on differential values of X, Y, Z, roll, pitch, yaw.
> 
> ![messageImage_1702377397219](https://github.com/Fzil0n/QuadCopter_simulation/assets/122668877/99a2c0b9-bafe-4758-93dd-eee1ea889626)

> ![messageImage_1702377463885](https://github.com/Fzil0n/QuadCopter_simulation/assets/122668877/197dc99a-d1ea-4d05-9998-150636515228)

> The libraries used for this visualization are Pygame for display creation and OpenGL for graphics rendering.
> 
# User Guide <a name="userguide"></a>
> 1. Within the Jupyter Notebook file, there are a total of 3 sections, consisting of:
> > - Section 1: Importing relevant packages into the project.
> > // Add pic
> > - Section 2 : The part where various parameters of the quadcopter are adjusted, using SI units. The adjustments should be made before clicking the "Run" button.
> > // Add pic
> > - Section 3 : Main loop witch operating at a frequency of 100 Hz.
> > // Add pic

> 2.  After clicking 'Run All,' the window as shown in the picture will appear.
> > // Add pic
> > After adjusting the speed of each motor successfully, press 'Start Sim' to enter the Visualization page.
> > // Add pic

> 3.  When visualization is complete, Program will shut down automatically.

# Demos & Result <a name="demosnresult"></a>
## Examples
> - Example 1: falling and spin about z-axis
>   
https://github.com/Fzil0n/QuadCopter_simulation/assets/122668877/f8c78fa3-a352-4a3c-b3cf-c508be4a07e9

> - Example 2: hover and spin about z-axis
> 
https://github.com/Fzil0n/QuadCopter_simulation/assets/122668877/dcd746c1-80fc-45e8-a3b5-ec25d120da76

### Validation
> - Animation compare with MATLAB
> > spin about z-axis
> > 
https://github.com/Fzil0n/QuadCopter_simulation/assets/122668877/c9a7a609-692d-4733-9779-8c53a8ceec56

> > spin about x-axis
> > 
https://github.com/Fzil0n/QuadCopter_simulation/assets/122668877/8194b8d3-2021-4189-b823-29aa6c514485

> - Dynamic compare with MATLAB
> > Spin about z-axis and hover
> > //add pic

# Conclusion <a name="conclusion"></a>
> Simulating the motion of a quadcopter using Python can be done using various libraries available in Python, such as NumPy, Matplotlib, and others, to model the dynamics of the quadcopter and visualize the results graphically. Comparing the results to MATLAB may show some differences depending on the simulation methods and parameters used in each system. However, by choosing appropriate parameters and using accurate simulation methods, you can achieve results that closely match those in MATLAB.
> 
> To enhance the reliability of your testing, you can experiment with refining and adjusting the parameters of the Python simulation to obtain results that closely align with the MATLAB outcomes. Testing that involves comparing results with MATLAB is a good step to verify the accuracy and reliability of your simulation.
> 
> Keep in mind that since there is no real-world quadcopter for direct comparison, testing can only be done by comparing results within the simulation environments, such as Python and MATLAB.

# Future plan <a name="futureplans"></a>
> - **Improve GUI and visualization.**
> - **Testing with real quadcopter.**
> - **Real-time speed adjustment and display of results.**
# Reference <a name="reference"></a>
> - [1] Lebedev, A. (2013). Design and Implementation of a 6DOF Control System for an Autonomous Quadrocopter (Master's thesis). Julius Maximilian University of Würzburg, Faculty of Mathematics and Computer Science, Aerospace Information Technology, Chair of Computer Science VIII, Prof. Dr. Sergio Montenegro.
> - [2] DRONE OMEGA, 2020, What is a Quadcopter Explained Thoroughly [Online], Available: [droneomega.com](https://droneomega.com/what-is-a-quadcopter/) [02/11/23]
> - [3] Pranav Bhounsule, 2020, Robotics Lec25,26: 3D quadcopter, derivation, simulation, animation (Fall 2020) [Online], Available: [YouTube](https://www.youtube.com/watch?v=4hlq2pf842u) [02/11/23]
> - [4] MATLAB, 2020, Drone Simulation and Control, Part 1: Setting Up the Control Problem [Online], Available: [YouTube](https://www.youtube.com/watch?v=hgcgpuqb67q) [02/11/23]
> - [5] Kanishke Gamagedara (2021). Plotting 3D Objects with Matplotlib. Github. https://github.com/kanishkegb/pyplot-3d
> - [6] P. Wang, Z. Man, Z. Cao, J. Zheng and Y. Zhao, "Dynamics modelling and linear control of quadcopter," 2016 International Conference on Advanced Mechatronic Systems (ICAMechS), Melbourne, VIC, Australia, 2016, pp. 498-503, doi: 10.1109/ICAMechS.2016.7813499.
> - [7] Ahmad, F., Kumar, P., & Patil, P. P. (2018). Modeling and simulation of a quadcopter with altitude and attitude control. Nonlinear Studies, 25(2), 287–299.
