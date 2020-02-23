import pygame
import math
import numpy as np
import os
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'

from car import Car
from racetrack import RaceTrack
from sensors import Sensors

from colors import *

pygame.init()

class Env():
    def __init__(self):
        self.displayWidth = 800
        self.displayHeight = 800
        self.title = 'CarAI'
        self.display = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.deltatime = self.clock.tick(60)

    def reset(self):
        self.car = Car()
        self.sensors = Sensors(self.car)
        self.raceTrack = RaceTrack()

    def step(self, action):
        #Action
        self.car.actionMove(action, self)
        #Car Step
        self.car.speed()
        self.car.move(self)
        self.car.nonRotatedRect()
        self.car.rotatedRect()
        #Sensor Step
        self.sensors.startCoord(self.car)
        self.sensors.sensorValues(self.car)
        self.sensors.intercept(self.raceTrack)

    def render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
                
        self.display.fill(white)
        self.raceTrack.update(self)
        self.car.drawCar(self)
        self.sensors.drawSensors(self)
        pygame.display.update()
