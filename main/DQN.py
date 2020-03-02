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
import tensorflow as tf


class DQNAgent(object):
    def __init__(self):
        self.epsilon = 1
        self.epsilon_dec = 0.995
        self.epsilon_min = 0.01
        self.ALPHA = 0.5 #Learning Rate
        self.GAMMA = 0.8 #Discount Factor
        self.EPISODES = 100_000

        self.batch_size = 64
        self.mem_size = 1000000

        self.state_size = 11
        self.action_size = 4
        self.action_space = [i for i in range(self.action_size)]

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

        self.model.compile(optimizer=Adam(lr=self.ALPHA), loss='mse')


    def main(self):
        for self.episode in range(self.EPISODES):
            score = 0
            done = False
            print('Episode:', self.episode)
            state = self.env.reset()
            while not done:
                #If random number between 0,1 is less that epsilon
                if random.uniform(0,1) < self.epsilon:
                    #Explore
                    action = np.random.choice(self.action_space)
                else:
                    pass
                    #Exploit
                    actions = self.model.predict(state_before)
                    action = np.argmax(actions)

                state_after, reward, done = self.env.step(action)

                score += reward

                learn
                action_values = np.array(self.action_space, dtype=np.int8)
                action_indices = np.dot(action, action_values)

                q_eval = self.model.predict(state_before)
                q_next = self.model.predict(state_after)

                q_target = model.copy()

                batch_index = np.array(self.batch_size, dtype=np.int32)

                q_target[batch_index, action_indices] = reward + self.GAMMA * np.max(q_next, axis=1) * done

                _ = self.q_eval.fit(state_before, q_target, verbose = 0)

                self.epsilon = self.epsilon * self.epsilon_dec if self.epsilon > self.epsilon_min else self.epsilon_min

                state_before = state_after

                if self.render:
                    self.env.render()



if __name__ == '__main__':
    dqnagent = DQNAgent()
