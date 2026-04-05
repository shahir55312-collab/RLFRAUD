from pydantic import BaseModel
from typing import List, Dict, Any

class Transactionobs(BaseModel):
    amount : float
    sender_country : str
    account_age_day : int
    is_flagged_by_system : bool

import gymnasium as gym
from gymnasium import spaces

import numpy as np

class AMLauditor(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2)
        self.current_case = None
    def reset(self):
        self.is_criminal = np.random.random() < 0.45
        if self.is_criminal:
            self.current_case = {
                "amount": np.random.uniform(1000, 10000),
               
                "account_age_day": np.random.randint(30, 150),
                "is_flagged_by_system": np.random.choice([0,1])
            }
        else:
            self.current_case = {
                "amount": 120.50,
                
                "account_age_day": 1000,
                "is_flagged_by_system": False

            }
        return self.state(),{}
    def step(self, action):
        if action == 1 and self.is_criminal:
            reward = 1.0
        elif action == 0 and not self.is_criminal:
            reward = 1.0
        elif action == 0 and  self.is_criminal:
            reward = -1.0
        else:
            reward = -0.5

        terminated = True
        return self.state(), reward, terminated, {}

    def state(self):
        return np.array([
            self.current_case["amount"],
            self.current_case["account_age_day"],
            int(self.current_case["is_flagged_by_system"])
        ])
    
def discrete_state(state):
    amount, account_age, flagged = state
    amount_bin = int(amount // 1000)
    account_age_bin = int(account_age // 30)
    flagged_bin = int(flagged)
    return (amount_bin, account_age_bin, flagged_bin)
env = AMLauditor()
Q = {}
alpha = 0.1
gamma =0.9
epsilon = 0.1
epsilon_decay = 0.99
epsilon_min = 0.01
episodes = 2000
for ep in range(episodes):
    state,_ = env.reset()
    state = discrete_state(state)
    if state not in Q:
        Q[state] = [0,0]


    if np.random.random() < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state])
    next_state,reward,terminated,_ = env.step(action)
    next_state = discrete_state(next_state)
    if next_state not in Q:
        Q[next_state] = [0,0]
    Q[state][action] = Q[state][action] + alpha * (reward + gamma * max(Q[next_state]) - Q[state][action])
    epsilon = max(epsilon * epsilon_decay, epsilon_min)
    if(ep+1) % 100 == 0:
        print(f"Episode {ep+1}, Epsilon: {epsilon:.4f}")

print("Testing Agent : ")
correct =0
total = 200
for _ in range(total):
    state,_ = env.reset()
    state = discrete_state(state)
    action = np.argmax(Q[state])
    _, reward, _, _ = env.step(action)
    if reward > 0:
        correct += 1

print(f"{correct}/{total} = {correct/total * 100:.2f}%")
