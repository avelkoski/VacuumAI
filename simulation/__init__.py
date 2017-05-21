# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import datetime
from time import sleep
from agents import Agent, Child
from environment import Environment
from plots import save_figure

class Simulation(object):
    def __init__(self,location,shape,plot):
        self.location = location
        self.shape = shape
        self.plot = plot
        self.env = Environment(self.shape)
        self.agent = Agent()
        self.child = Child(self.env.state)

    def run(self,duration):
        start = datetime.now()
        self.env.state = self.child.run()
        self.agent.on()
        if self.plot: save_figure(self.env.x,self.env.y,self.env.state,[self.agent.position[0]],[self.agent.position[1]])
        while self.agent.active:
            self.agent.precepts(self.env.state)
            self.env.state = self.agent.effectors(self.env.state)
            if self.plot: save_figure(self.env.x,self.env.y,self.env.state,[self.agent.position[0]],[self.agent.position[1]])
            else: sleep(0.5)
            if (datetime.now() - start).seconds >= duration:
                self.agent.gohome()
                self.agent.precepts(self.env.state)
                self.env.state = self.agent.effectors(self.env.state)
                if self.plot: save_figure(self.env.x,self.env.y,self.env.state,[self.agent.position[0]],[self.agent.position[1]])
                else: sleep(0.5)
        rwd, clnd = self.agent.reward, self.agent.cleaned
        self.agent.reset()
        return rwd, clnd
