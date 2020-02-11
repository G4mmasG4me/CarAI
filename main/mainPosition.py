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
EPISODES = 1000
WALL_PENALTY = 50
CHECKPOINT_REWARD = 10

epsilon = 0.9
EPSILON_DECAY = 0.9999

ALPHA = 0.1 #Learning Rate
GAMMA = 0.9 #Discount Factor

state_size = [800, 800]
action_size = 4
Q = np.zeros(state_size +  [action_size])

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
            print('EP:', episode)
            car = Car()
            raceTrack = RaceTrack()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                state = (car.x, car.y)
                if random.uniform(0,1) < epsilon:
                    #Explore
                    action = np.random.randint(action_size)
                else:
                    #Exploit
                    action = np.argmax(Q[state])
                car.actionMove(action, self)

                self.display.fill(white)
                car.update(self, raceTrack)
                raceTrack.update(self)
                pygame.display.update()
                self.deltatime = self.clock.tick(60)

                crash = car.wallCollision(raceTrack)
                if crash == True:
                    #Car Collides with Wall
                    reward = -WALL_PENALTY
                    print('Crash')
                elif car.checkpointCollision(raceTrack) == True:
                    #Car Colldies with Checkpoint
                    reward = CHECKPOINT_REWARD
                    print('Gone Through Checkpoint')
                else:
                    #Car Doesn't Collide
                    #Could implement a movement penalty
                    reward = 0

                new_state = (car.x, car.y)
                max_future_q = np.max(Q[new_state])
                current_q = Q[state][action]

                if reward == CHECKPOINT_REWARD:
                    new_q = CHECKPOINT_REWARD
                else:
                    new_q = (1 - ALPHA) * current_q + ALPHA * (reward + GAMMA * max_future_q)
                Q[state][action] = new_q

                if reward == -WALL_PENALTY:
                    break

            epsilon *=EPSILON_DECAY

if __name__ == '__main__':
    Main = Main()
