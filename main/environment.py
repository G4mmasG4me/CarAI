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
        self.deltatime = 1

    def reset(self):
        self.car = Car(self)
        self.raceTrack = RaceTrack()
        self.sensors = Sensors(self.car, self.raceTrack)
        self.car.update(self)
        self.sensors.update(self.car, self.raceTrack)

        carState = self.car.getState()
        sensorState = self.sensors.getState()

        state = sensorState + [carState]
        state = np.array(state)
        state = state[np.newaxis, :]

        state = state[0]
        return state


    def step(self, action):
        #Action
        self.car.actionMove(action, self)
        #Car Step
        angle = self.car.update(self)
        #Sensor Step
        self.sensors.update(self.car, self.raceTrack)

        carState = self.car.getState()
        sensorState = self.sensors.getState()

        state = sensorState + [carState]
        state = np.array(state)
        state = state[np.newaxis, :]

        state = state[0]

        reward = 0
        done = False
        if self.car.wallCollision(self.raceTrack):
            reward = -50
            done = True
        if self.car.checkpointCollision(self.raceTrack):
            reward = 10

        return state, reward, done

    def render(self):
        try:
            self.display
        except AttributeError:
            self.display = None

        if self.display is None:
            self.display = pygame.display.set_mode((self.displayWidth, self.displayHeight))
            pygame.display.set_caption(self.title)
            self.clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

        self.deltatime = self.clock.tick(60)
        self.display.fill(white)
        self.raceTrack.update(self)
        self.car.drawCar(self)
        self.sensors.drawSensors(self)
        pygame.display.update()
