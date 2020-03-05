import numpy as np
import random

from pathlib import Path

from environment import Env
from car import Car
from racetrack import RaceTrack
from sensors import Sensors

#Machine Learning
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.optimizers import Adam
import tensorflow as tf

from collections import deque

from tqdm import tqdm


class DQNAgent(object):
    def __init__(self):
        self.epsilon = 1
        self.EPSILON_DEC = 0.9999
        self.EPSILON_MIN = 0.01
        self.ALPHA = 0.5 #Learning Rate
        self.GAMMA = 0.8 #Discount Factor
        self.EPISODES = 100_000

        model_name = 'Model.h5'
        target_model_name = 'TargetModel.h5'

        self.model_path = Path('models/saved/' + target_model_name)
        self.target_model_path = Path('models/inuse/' + target_model_name)

        self.UPDATE_TARGET_EVERY = 5
        self.target_update_counter = 0

        self.RENDER_EVERY = 10
        self.SAVE_EVERY = 100

        self.REPLAY_MEMORY_SIZE = 100_000
        self.MIN_REPLAY_MEMORY_SIZE = 1_000
        self.MINIBATCH_SIZE = 64

        self.state_size = 11
        self.action_size = 4
        self.action_space = [i for i in range(self.action_size)]

        self.replay_memory = deque(maxlen=self.REPLAY_MEMORY_SIZE)

        self.env = Env()

        self.render = True
        if self.model_path.is_file() and self.target_model_path.is_file():
            self.model = load_model(self.model_path)
            self.target_model = load_model(self.target_model_path)
        else:
            self.model = self.buildDQN()
            self.target_model = self.buildDQN()
            self.target_model.set_weights(self.model.get_weights())
        self.main()

    def buildDQN(self):
        model = Sequential()
        model.add(Dense(256, input_shape=(self.state_size, )))
        model.add(Activation('relu'))
        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(Dense(self.action_size))

        model.compile(optimizer=Adam(lr=self.ALPHA), loss='mse', metrics=['accuracy'])

        return model

    def update_replay_memory(self, transition):
        self.replay_memory.append(transition)

    def train(self, terminal_state):
        if len(self.replay_memory) < self.MIN_REPLAY_MEMORY_SIZE:
            return

        minibatch = random.sample(self.replay_memory, self.MINIBATCH_SIZE)

        current_states = np.array([transition[0] for transition in minibatch])
        current_qs_list = self.model.predict(current_states)

        new_current_states = np.array([transition[3] for transition in minibatch])
        future_qs_list = self.target_model.predict(new_current_states)

        x = []
        y = []

        for index, (current_state, action, reward, new_current_state, done) in enumerate(minibatch):
            if not done:
                max_future_q = np.max(future_qs_list[index])
                new_q = reward + self.GAMMA * max_future_q
            else:
                new_q = reward

            current_qs = current_qs_list[index]
            current_qs[action] = new_q

            x.append(current_state)
            y.append(current_qs)

        self.model.fit(np.array(x), np.array(y), batch_size=self.MINIBATCH_SIZE, verbose=0)

        if terminal_state:
            self.target_update_counter += 1

        if self.target_update_counter > self.UPDATE_TARGET_EVERY:
            self.target_model.set_weights(self.model.get_weights())
            self.target_update_counter = 0

    def get_qs(self, state):
        state = np.array(state)
        state = state.reshape(1, -1)
        return self.model.predict(state)

    def main(self):
        for self.episode in tqdm(range(self.EPISODES), unit='episodes'):
            score = 0
            done = False
            current_state = self.env.reset()
            while not done:
                #If random number between 0,1 is less that epsilon
                if np.random.random() < self.epsilon:
                    #Explore
                    action = np.random.choice(self.action_space)
                else:
                    pass
                    #Exploit
                    action = np.argmax(self.get_qs(current_state))

                new_state, reward, done = self.env.step(action)

                if self.render and not self.episode % self.RENDER_EVERY:
                    self.env.render()

                self.update_replay_memory((current_state, action, reward, new_state, done))
                self.train(done)

                current_state = new_state

            if not self.episode % self.SAVE_EVERY:
                self.model.save(self.model_path)
                self.target_model.save(self.target_model_path)

            if self.epsilon > self.EPSILON_MIN:
                self.epsilon *= self.EPSILON_DEC
                self.epsilon = max(self.EPSILON_MIN, self.epsilon)



if __name__ == '__main__':
    agent = DQNAgent()
