import pygame
import math
import numpy as np
import os
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,25'
#Objects
from car import Car
from racetrack import RaceTrack
from sensors import Sensors

pygame.init()
#pygame.mixer.init()

#Music to play
file = 'TokyoDrift.mp3'
#pygame.mixer.music.load(file)
#pygame.mixer.music.play()

#Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#DQN Variables
EPISODES = 10000
WALL_PENALTY = 50
CHECKPOINT_REWARD = 10

epsilon = 0.99
EPSILON_DECAY = 0.999

ALPHA = 0.1 #Learning Rate
GAMMA = 0.9 #Discount Factor

state_size = (200, 200)
action_size = 4

#Q = np.zeros(state_size +  [action_size])
Q = np.zeros(state_size +  (action_size,), dtype=float)


class Main():
    def __init__(self):
        self.displayWidth = 800
        self.displayHeight = 800
        self.title = 'CarAI'
        self.display = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.deltatime = self.clock.tick(60)
        self.running = True
        self.main()


    def main(self):
        epsilon = 0.9
        for episode in range(EPISODES):
            reward = 0
            print('Start | EP:', episode, '| Epsilon:', epsilon)
            car = Car()
            sensors = Sensors(car)
            raceTrack = RaceTrack()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                self.display.fill(white)
                car.update(self, raceTrack)
                sensors.update(car, raceTrack, self)
                raceTrack.update(self)
                pygame.display.update()
                self.deltatime = self.clock.tick(60)


if __name__ == '__main__':
    Main = Main()
