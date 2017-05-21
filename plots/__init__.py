#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 20 22:40:04 2017

@author: avelkoski
"""

import matplotlib.pyplot as plt
from imageio import imread, mimsave
from os import listdir, remove
from datetime import datetime
from config import location, filetype, gifname, marker, markersize,figsize,dpi

def save_figure(x,y,state,position1,position2):
    fig = plt.figure(figsize=figsize,dpi=dpi)
    plt.contourf(x,y,state)
    plt.plot([position1],[position2],marker,markersize=markersize)
    fig.savefig(''.join([location,str(datetime.now()),filetype]))

def gif(run):
    images = []
    filenames = [x for x in listdir(location) if filetype in x]
    filenames.sort()
    for filename in filenames:
        fqfn = ''.join([location,filename])
        images.append(imread(fqfn))
        remove(fqfn)
    fqgn = ''.join([location,gifname,str(run),'.gif'])
    mimsave(fqgn, images)
