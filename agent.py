import torch
import random
import numpy as np
from snake import SnakeGame, Direction, Point
from collections import deque

MAX_MEMORY = 100000
BATCH_SIZE = 1000
LR = 0.001


class Agent:


    def __init__(self):
        self.n_games = 0
        self.epsilon = 0    #controls randomness
        self.gamma = 0      #discount rate
        self.memory = deque(maxlen=MAX_MEMORY)


    def get_state(self, game):
        pass


    def remember(self, state, action, reward, next_state, done):
        pass


    def train_long_memory(self):
        pass


    def train_short_memory(self, state, action, reward, next_state, done):
        pass


    def get_action(self, state):
        pass


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGame()
    while True:
        #get old state
        state_old = agent.get_state(game)

        #get move
        final_move = agent.get_action(state_old)

        #move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        #train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        #remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            #train long memory and plot results
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                #agent.model.save()

            print("game: ", agent.n_games, " score: ", score, " record ", record)
            


if __name__ = '__main__':
    train()

    
