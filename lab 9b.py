#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:03:41 2024

@author: eltc-paul
"""

import random

class Agent:
    def __init__(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agents = []

        for _ in range(num_agents):
            while True:
                x, y = random.randint(0, size-1), random.randint(0, size-1)
                if self.grid[y][x] is None:
                    agent = Agent((x, y))
                    self.agents.append(agent)
                    self.grid[y][x] = agent
                    break

    def find_empty_patch(self):
        empty_patches = [(x, y) for x in range(self.size) for y in range(self.size) if self.grid[y][x] is None]
        return random.choice(empty_patches) if empty_patches else None

    def move_agent(self, agent):
        new_position = self.find_empty_patch()
        if new_position:
            self.grid[agent.position[1]][agent.position[0]] = None 
            agent.move(new_position)
            self.grid[new_position[1]][new_position[0]] = agent  

    def simulate(self):
        for _ in range(13):  
            for agent in self.agents:
                self.move_agent(agent)


world = World(size=5, num_agents=3)  
world.simulate()


for agent in world.agents:
    print(f"Agent at position {agent.position}")

