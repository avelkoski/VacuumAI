#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:30:58 2017

@author: avelkoski
"""

from numpy import array, min, random, max, where
from config import rewards

class Agent(object):
    def __init__(self):
        self.active = False
        self.home = array([0,0])
        self.position = array([0,0])
        self.orientation = 0
        self.step = {0:array([0,1]),90:array([1,0]),180:array([0,-1]),270:array([-1,0])}
        self.precept = (False, False, False)
        self.reward = 0
        self.cleaned = 0

    def on(self):
        self.active = True
        self.position = self.position + self.step[self.orientation]

    def off(self):
        if not (self.position == self.home).all():
            self.reward -= 1000
        self.active = False

    def reset(self):
        self.position == self.home
        self.active = False
        self.orientation = 0
        self.reward = 0
        self.cleaned = 0
        self.precept = (False, False, False)

    def precepts(self,state):
        touchsense, photosense, infrasense = self.precept
        if min(self.position) < 0 or max(self.position) > 7:
            touchsense = True
        elif state[self.position[1],self.position[0]]==1:
            photosense = True
        elif (self.position == self.home).all():
            infrasense = True
        self.precept = (touchsense,photosense,infrasense)

    def payoff(self,state,rewards=rewards):
        fwd,p90,n90 = self.orientation, (self.orientation + 90) % 360, (self.orientation - 90) % 360
        results=[]
        for orientation in [fwd,p90,n90]:
            reward = 0
            step = self.position + self.step[orientation]
            touchsense, photosense, infrasense = (False,False,False)
            if min(step) < 0 or max(step) > 7:
                touchsense = True
                reward -= rewards['touch']
            elif state[step[1],step[0]]==1:
                photosense = True
                reward += rewards['photo']
            elif (step == self.home).all():
                infrasense = True
                reward -= rewards['infra']
            else:
                reward -= rewards['move']
            results.append({'orientation':orientation,'reward':reward})
        rewards = array([x['reward'] for x in results])
        indices = array(where(rewards==rewards.max())[0])
        index = random.choice(indices)
        return results[index]

    def effectors(self,state,rewards=rewards):
        touchsense, photosense, infrasense = self.precept
        if infrasense:
            self.off()
            self.reward -= rewards['infra']
        elif touchsense:
            self.orientation = self.payoff(state)['orientation']
            self.precept = (False,photosense,infrasense)
            self.reward -= rewards['touch']
        elif photosense:
            state[self.position[1],self.position[0]] = 0
            self.precept = (touchsense,False,infrasense)
            self.reward += rewards['photo']
            self.cleaned += 1
        else:
            optimal = self.payoff(state)['orientation']
            if self.orientation == optimal:
                self.position = self.position + self.step[self.orientation]
                self.reward -= rewards['move']
            else:
                self.orientation = optimal
                self.reward -= rewards['move']
        return state

    def gohome(self):
        touchsense, photosense, infrasense = self.precept
        if self.position[1] > 0:
            self.orientation = 180
            self.position = self.position + self.step[self.orientation]
        elif self.position[0] > 0:
            self.orientation = 270
            self.position = self.position + self.step[self.orientation]


class Child(object):
    def __init__(self,state):
        self.state = state

    def run(self):
        for i in xrange(self.state.shape[0]):
            for j in xrange(self.state.shape[0]):
                self.state[i,j] = random.randint(2)
        return self.state
