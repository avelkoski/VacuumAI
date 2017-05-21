#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:29:37 2017

@author: avelkoski
"""
from numpy import array, arange, zeros, meshgrid
from config import indexing

class Environment(object):
    """Environment"""
    def __init__(self,shape):
        self.shape = array(shape)
        self.x = arange(self.shape[0])
        self.y = arange(self.shape[1])
        self.xv, self.yv = meshgrid(self.x,self.y,indexing=indexing)
        self.state = zeros(shape=(self.shape[0],self.shape[1]))
