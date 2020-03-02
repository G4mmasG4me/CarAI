import numpy as np
import random

from environment import Env
from car import Car
from racetrack import RaceTrack
from sensors import Sensors

#Machine Learning
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam


class DQNAgent(object):
    def __init__(self):
        self.epsilon = 0.75
        self.ALPHA = 0.5 #Learning Rate
        self.GAMMA = 0.8 #Discount Factor
        self.EPISODES = 100_000

        self.state_size = 11
        self.action_size = 4

        self.env = Env()

        self.render = True
        self.buildDQN()
        self.main()

    def buildDQN(self):
        self.model = Sequential()
        self.model.add(Dense(256, input_shape=(self.state_size, )))
        self.model.add(Activation('relu'))
        self.model.add(Dense(256))
        self.model.add(Activation('relu'))
        self.model.add(Dense(self.action_size))


    def main(self):
        for self.episode in range(self.EPISODES):
            reward = 0
            alive = True
            print('Episode:', self.episode)
            self.env.reset()
            state_before = self.env.step(4)
            while alive:
                #If random number between 0,1 is less that epsilon
                if random.uniform(0,1) < self.epsilon:
                    #Explore
                    action = np.random.randint(self.action_size)
                else:
                    pass
                    #Exploit
                    state_before = np.array(state_before)
                    state_before = state_before[np.newaxis, :]
                    actions = self.model.predict(state_before)
                    action = np.argmax(actions)

                state_after = self.env.step(action)

                #Do stuff here

                state_before = state_after

                if self.render:
                    self.env.render()

                if self.env.car.wallCollision(self.env.raceTrack):
                    reward -= 50
                    alive = False
                if self.env.car.checkpointCollision(self.env.raceTrack):
                    reward += 10

if __name__ == '__main__':
    dqnagent = DQNAgent()
