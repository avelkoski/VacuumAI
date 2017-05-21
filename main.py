#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 09:33:39 2017

@author: avelkoski
"""

from sys import argv, exit
from numpy import mean
from simulation import Simulation
from plots import gif
from config import location, shape

def main():
    if len(argv)==4:
        runs = int(argv[1])
        duration = int(argv[2])
        plot = int(argv[3])
    else:
        print 'Runs, Duration, and Plotting Args Required'
        exit(-1)

    sim = Simulation(location,shape,plot)

    rwds,clnd = [],[]
    for i in xrange(runs):
        rwd, cln = sim.run(duration)
        rwds.append(rwd), clnd.append(cln)
        if plot: gif(i)

    print 'Average Reward: ' + str(mean(rwds))
    print 'Average Cells Cleaned: ' + str(mean(clnd))

if __name__ == "__main__":
   main()
