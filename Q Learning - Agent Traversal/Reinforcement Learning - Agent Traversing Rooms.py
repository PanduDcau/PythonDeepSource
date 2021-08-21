#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


# In[2]:


#initializing the Agent Matrix
agent = np.array ([[-1,-1,-1,-1,0,-1],
                   [-1,-1,-1,0,-1,100],
                   [-1,-1,-1,0,-1,-1],
                   [-1,0,0,-1,0,-1],
                   [0,-1,-1,0,-1,100],
                   [-1,0,-1,-1,0,100]])


# In[3]:


pd.DataFrame(agent)


# In[4]:


# Creating a 6x6 matrix with 0 to initialzing the Q Table
def initialize_q(m,n):
    return np.zeros((m,n))

#Using Pands for Display Purpose
qmatrix = initialize_q(6,6)
pd.DataFrame(qmatrix)


# In[5]:


#denoting rooms as 6 according to problem
def set_initial_state(rooms =6):
    
    #Store the initial State
    return np.random.randint(0, rooms)

#initializing the action to be implement from the matrix
def get_action(current_state, agent_mat):
    
    #Given a State, Choose from the Possiable
    valid_actions = []
    for action in enumerate(agent_mat[current_state]):
        if action[1] !=-1:
            valid_actions +=[action[0]]
    return random.choice(valid_actions)

def take_act(current_state, agent_mat,gamma, verbose = False):
    
    #Take a Single Action
    action = get_action(current_state, agent_mat)
    sa_reward= agent_mat[current_state,action] #Current State-action Reward
    ns_reward= max(qmatrix[action,]) #Next State-action Reward
    print(ns_reward)
    q_cur_state = sa_reward + (gamma * ns_reward) #Current state will be updated with the actions done 
    qmatrix[current_state, action] = q_cur_state #  Mutates q Matrix
    new_state = action
    if verbose:
        print(qmatrix)
        print(f"Old State: {current_state} | New State : {new_state}\n\n")
        if new_state == 5:   #When new State get to room 5 , Agent will stop the traversal 
            print(f" Agent Has Reached their Goal !!! ")
    return new_state


# In[6]:


def initial_episode(agent_mat,initial_state, gamma, verbose =False):
    
    # Runs 1 episode (or Simulation) until the agent reach it's goal-state
    
    current_state = initial_state
    while True: # We won't use cureent state == 5 because possiable to initialize in 5
        current_state = take_act(current_state, agent_mat, gamma , verbose)
        if current_state == 5:
            break
                                    
def train_agent(iteration , agent_mat , gamma , verbose: False): #Training the agent for q-learning
        
        #Runs a given number of episodes then normalize the matrix
        print("Training in Progress>>>>")
        for episode in range(iteration):
            initial_state = set_initial_state()
            initial_episode(agent_mat, initial_state, gamma, verbose)
        print("Training Complete! >>")
        
        return qmatrix


# In[7]:


#Normalizing the q matrix for get a simplified 2D table
def normalize_mat(qmatrix):
    normalized_q=qmatrix / max(qmatrix[qmatrix.nonzero()])*100
    return normalized_q.astype(int)


# In[8]:


# Test Run of Single Episode
gamma = 0.1
initial_state = 2
initial_action = get_action(initial_state, agent)

initial_episode(agent, initial_state, gamma, True)


# In[11]:


#Test Run Full Training  (Training= 2000 iterations)
gamma = 0.8
initial_state=set_initial_state()
initial_action = get_action(initial_state, agent)

q_table = train_agent(2000, agent, gamma, False)

# Creating DataFrame for Display Purpose
pd.DataFrame(q_table)


# In[25]:


#summerized the column vector values after training ends
plt.plot(q_table[1]) #Room no 1's Finalized score
plt.xlabel('Room Number')
plt.ylabel("Q-Score")
plt.show


# In[55]:


#Normalizing the Dataframe

pd.DataFrame(normalize_mat(q_table))


# In[16]:


#After the training is done , we deploy the agent from this agent
def deploy_agent(init_state, q_table):
    print("Start: ",init_state)
    state = init_state
    steps =0
    while True:
        steps += 1
        action = np.argmax(q_table[state,:])  # Filtering out the maximum values from the normalized q Table
        print(action)
        state= action
        if action == 5:
            print("Finished the Searching")
            return steps


# In[17]:


#Lets Run an Example 1
start_room = 2  #insert the Starting room for agent to start
steps = deploy_agent(start_room,q_table)
print("Number of Rooms/ Actions: ", steps)


# In[15]:


#Lets Run an Example 2
start_room = 0  #insert the Starting room for agent to start
steps = deploy_agent(start_room,q_table)
print("Number of Rooms/ Actions: ", steps)


# In[ ]:




