#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:32:23 2017

@author: avelkoski
"""

## nxn Environment
shape = (8,8)
indexing = 'ij'

## Locations 
location = '/home/avelkoski/Downloads/'
filetype = '.png'
gifname = 'simulation'

## Plot settings
marker = 'ro'
markersize = 20
figsize=(8,6)
dpi = 100

## Rewards
rewards = {'touch':10,'photo':100,'infra':5,'move':1}