import numpy as np

#setting variables
epsilon = 0.75
alpha = 0.5 #learning rate
gamma = 0.8

#Sets Q table to all 0s
state_size = 12
action_size = 4
Q = np.zeros((state_size, action_size))
print(Q)

#If random number between 0,1 is less that epsilon
if random.uniform(0,1) < epsilon:
    #Explore
    action = env.action_space.sample()
    action = np.random.randint(0, env.action_space.n)
else:
    #Exploit
    action = np.argmax(Q[state])

#Updating Q Values
#Q(state,action)<--(1-a)Q(state,action) + a(reward + y*maxQ(next state, all actions))
Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])

#step Function
#return np.array(self.state), reward, done, {}

#reset Function
#return np.array(self.state)

#render Function
#return self.viewer.render(return_rgb_array = mode=='rgb_array')

#close Function
