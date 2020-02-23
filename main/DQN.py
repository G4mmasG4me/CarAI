import numpy as np
import random

from environment import Env
from car import Car
from racetrack import RaceTrack
from sensors import Sensors

#Setting Variables
epsilon = 0.75
alpha = 0.5 #learning rate
gamma = 0.8 #discount factor
EPISODES = 100

#Q Table Sizes
state_size = 12
action_size = 4

#Q Table
Q = np.zeros((state_size, action_size))

env = Env()

render = True

for episode in range(EPISODES):
    running = True
    env.reset()
    while running:
        #If random number between 0,1 is less that epsilon
        if random.uniform(0,1) < epsilon:
            #Explore
            action = np.random.randint(action_size)
        else:
            pass
            #Exploit
            #action = np.argmax(Q[state])
        env.step(action)

        if render:
            env.render()

#Updating Q Values
#Q(state,action)<--(1-a)Q(state,action) + a(reward + y*maxQ(next state, all actions))

#step Function
#return np.array(self.state), reward, done, {}

#reset Function
#return np.array(self.state)

#render Function
#return self.viewer.render(return_rgb_array = mode=='rgb_array')

#close Function
