import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import cos, sin, pi
import tkinter as tk
import time


class Quadcopter3DVisualization:
    def __init__(self):
        # Initialize Pygame and set up the display
        pygame.init()
        self.display = (1280, 500)
        pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Quadcopter 3D Visualization")

        # Set up the initial perspective
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)

        # Store quadcopter positions over time
        self.quadcopter_positions = []

    def draw_circle(self, radius, segments):
        glBegin(GL_POLYGON)
        for i in range(segments):
            theta = 2.0 * pi * i / segments
            x = radius * cos(theta)
            y = radius * sin(theta)
            glVertex3f(x, y, 0)
        glEnd()

    def draw_quadcopter(self, roll, pitch, yaw, x, y, z):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glTranslatef(x, y, z)
        glRotatef(yaw, 0, 1, 0)
        glRotatef(pitch, 1, 0, 0)
        glRotatef(roll, 0, 0, 1)

        # Draw intersecting lines representing quadcopter arms
        glBegin(GL_LINES)
        glColor3f(1.0, 0.0, 0.0)  # Red
        glVertex3f(-0.25, 0, 0)  # Left arm
        glVertex3f(0.25, 0, 0)
        glEnd()

        # Draw circles at the end of the arms
        glColor3f(1.0, 1.0, 1.0)  # White
        glPushMatrix()
        glTranslatef(-0.25, 0, 0)
        self.draw_circle(0.05, 30)  # Adjust the radius and segments as needed
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0.25, 0, 0)
        self.draw_circle(0.05, 30)  # Adjust the radius and segments as needed
        glPopMatrix()

        glColor3f(0.0, 1.0, 0.0)  # Green
        glBegin(GL_LINES)
        glVertex3f(0, -0.25, 0)  # Back arm
        glVertex3f(0, 0.25, 0)
        glEnd()

        # Draw circles at the end of the back arm
        glColor3f(1.0, 1.0, 1.0)  # White
        glPushMatrix()
        glTranslatef(0, -0.25, 0)
        self.draw_circle(0.05, 30)  # Adjust the radius and segments as needed
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.25, 0)
        self.draw_circle(0.05, 30)  # Adjust the radius and segments as needed
        glPopMatrix()

        # Draw an arrow indicating the quadcopter's front
        glBegin(GL_LINES)
        glColor3f(0.5, 1.0, 1.5)  # Blue
        glVertex3f(0, 0, 0)  # Center
        glVertex3f(0.125, -0.125, 0)  # Front
        glEnd()

        # Draw a 3D box in the middle of the drone
        box_size = 0.04
        glBegin(GL_QUADS)
        glColor3f(0.0, 1.0, 0.0)  # Green
        glVertex3f(-box_size, -box_size, -box_size)
        glVertex3f(box_size, -box_size, -box_size)
        glVertex3f(box_size, box_size, -box_size)
        glVertex3f(-box_size, box_size, -box_size)

        glVertex3f(-box_size, -box_size, box_size)
        glVertex3f(box_size, -box_size, box_size)
        glVertex3f(box_size, box_size, box_size)
        glVertex3f(-box_size, box_size, box_size)

        glVertex3f(-box_size, -box_size, -box_size)
        glVertex3f(box_size, -box_size, -box_size)
        glVertex3f(box_size, -box_size, box_size)
        glVertex3f(-box_size, -box_size, box_size)

        glVertex3f(-box_size, box_size, -box_size)
        glVertex3f(box_size, box_size, -box_size)
        glVertex3f(box_size, box_size, box_size)
        glVertex3f(-box_size, box_size, box_size)

        glVertex3f(-box_size, -box_size, -box_size)
        glVertex3f(-box_size, box_size, -box_size)
        glVertex3f(-box_size, box_size, box_size)
        glVertex3f(-box_size, -box_size, box_size)

        glVertex3f(box_size, -box_size, -box_size)
        glVertex3f(box_size, box_size, -box_size)
        glVertex3f(box_size, box_size, box_size)
        glVertex3f(box_size, -box_size, box_size)
        glEnd()

        # Store the quadcopter position
        self.quadcopter_positions.append((roll, pitch, yaw, x, y, z))

        glPopMatrix()
        pygame.display.flip()

class QuadcopterController:
    def __init__(self, quadcopter_visualization):
        self.quadcopter_visualization = quadcopter_visualization
        self.quadcopter_state = [0, 0, 0, 0, 0, 0]

    # def update_quadcopter_and_plot(self):

    #     # Update quadcopter state
    #     self.quadcopter_state = [
    #         self.quadcopter_state[0] + deltas[0],
    #         self.quadcopter_state[1] + deltas[1],
    #         self.quadcopter_state[2] + deltas[2],
    #         self.quadcopter_state[3] + deltas[3],
    #         self.quadcopter_state[4] + deltas[4],
    #         self.quadcopter_state[5] + deltas[5]
    #     ]

    #     self.quadcopter_visualization.draw_quadcopter(*self.quadcopter_state)
    def update_quadcopter_and_plot(self,state:list[float])->None:
        # Update quadcopter state
        self.quadcopter_state = state
        self.quadcopter_visualization.draw_quadcopter(*self.quadcopter_state)

deltas = [0, 0, 0, 5, 2, 0]

quadcopter_visualization = Quadcopter3DVisualization()
quadcopter_controller = QuadcopterController(quadcopter_visualization)
while(1):
    quadcopter_controller.update_quadcopter_and_plot(deltas)
    # deltas[0] += 0.01
    time.sleep(0.1)