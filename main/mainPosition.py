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
from colors import *

#DQN Variables
EPISODES = 10000
WALL_PENALTY = 50
CHECKPOINT_REWARD = 10

epsilon = 0.99
EPSILON_DECAY = 0.999

ALPHA = 1 #Learning Rate
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
            raceTrack = RaceTrack()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                before_action_state = (int(round(car.x, 0) / 4), int(round(car.y, 0) / 4))
                if random.uniform(0,1) < epsilon:
                    #Explore
                    action = np.random.randint(action_size)
                else:
                    #Exploit
                    action = np.argmax(Q[before_action_state])

                car.actionMove(action, self)

                self.display.fill(white)
                car.update(self, raceTrack)
                raceTrack.update(self)
                pygame.display.update()
                self.deltatime = self.clock.tick(60)

                crash = car.wallCollision(raceTrack)
                if crash == True:
                    #Car Collides with Wall
                    reward -= WALL_PENALTY
                    break
                checkpoint = car.checkpointCollision(raceTrack)
                if checkpoint == True:
                    #Car Colldies with Checkpoint
                    reward += CHECKPOINT_REWARD

                after_action_state = (int(round(car.x, 0) / 4), int(round(car.y, 0) / 4))
                best_q = np.amax(Q[after_action_state])

                Q[before_action_state + (action,)] = ALPHA * (reward + GAMMA * best_q)

            print('End | EP:', episode, '| Score:', reward, '\n')
            epsilon *=EPSILON_DECAY

if __name__ == '__main__':
    Main = Main()
