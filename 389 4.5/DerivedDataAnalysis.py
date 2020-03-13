import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FullDataSet = pd.read_pickle(r'h:/3rd Year Python/389 4.0/cyclotrondata') 

def averagepositionplot():
    xpos = []
    ypos = []
    zpos = []
    for i in range(len(FullDataSet.AveragePosition)):
        xpos.append(FullDataSet.AveragePosition[i][0])
        ypos.append(FullDataSet.AveragePosition[i][1])
        zpos.append(FullDataSet.AveragePosition[i][2])
    fig = plt.axes(projection = '3d', xlabel = 'x', ylabel = 'y', zlabel = 'z')
    fig.plot3D(xpos,ypos,zpos)
    plt.show()

def averagevelocityplot():
    plt.plot(FullDataSet.Time, FullDataSet.AverageSpeed)
    plt.show()

def averageenergyplot():
    plt.plot(FullDataSet.Time, FullDataSet.AverageEnergy)
    plt.show()

def energyspreadplot():
    plt.plot(FullDataSet.Time,FullDataSet.EnergySpread/constants.elementary_charge)
    plt.show()

def CyclotronFrequency():
    timelist = []
    listofdirection = [0,0]
    for i in range(len(FullDataSet.AveragePosition)):
        listofdirection[i%2] = FullDataSet.AveragePosition[i][2] / (-1)
        if listofdirection[0] != listofdirection[1]:
            timelist.append(FullDataSet.Time[i])
    FreqList = []
    for i in range(len(timelist)-1):
        Period = timelist[i+1] -timelist[i]
        FreqList.append((2*np.pi)/Period)
    timelist.pop(0)
    plt.plot(timelist, FreqList)
    plt.show()


def finalstateofparticle():
    final = len(FullDataSet.AveragePosition) - 1
    print('The Final state of the bunch is : Radius of orbit = %s, Velocity of bunch = %s, Average Energy in ev  = %s, Spread of the bunch = %s'
        %(np.linalg.norm(FullDataSet.AveragePosition[final]),FullDataSet.AverageSpeed[final], FullDataSet.AverageEnergy[final],FullDataSet.Spread[final]))

energyspreadplot()