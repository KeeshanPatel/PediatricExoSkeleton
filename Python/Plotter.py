# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:27:57 2017

@author: debian
"""

import matplotlib.pyplot as plt
import numpy as np
import time
import write
import os

plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate (inputstring,number,color):
    filename = "Data_Trial_"+ str(color) + "_" + str(number) +".txt"
    #pullData = open(os.path.join(write.DataFolder,filename),"r").read()
    pullData = open(filename,"r").read()
    dataArray =pullData.split('\n')
    xar=[]
    xar = [int(numstr) for numstr in dataArray]
    yar=[]
    y = 0
    for eachline in dataArray:
        yar.append(y)
        y =y+1
    ax1.clear()
    ax1.plot(xar,yar)
