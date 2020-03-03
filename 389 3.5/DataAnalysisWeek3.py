import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FullDataSet = pd.read_pickle(r'h:/3rd Year Python/389 3.0/cyclotrondata')

def PositionPlot():
    xpos = []
    ypos = []
    zpos = []
    for i in range(len(FullDataSet.position)):
        xpos.append(FullDataSet.position[i][0])
        ypos.append(FullDataSet.position[i][1])
        zpos.append(FullDataSet.position[i][2])
    fig = plt.axes(projection = '3d', xlabel = 'x', ylabel = 'y', zlabel = 'z')
    fig.plot3D(xpos,ypos,zpos)
    plt.show()

def VelocityPlot():
    speedlist = []
    for i in range(len(FullDataSet.velocity)):
        speed = np.linalg.norm(FullDataSet.velocity[i])
        speedlist.append(speed)
    plt.plot(FullDataSet.Time, speedlist)
    plt.show()

def FieldAgainstPosition():
    efield = []
    xpos = []
    for i in range(len(FullDataSet.position)):
        xpos.append(FullDataSet.position[i][0])
        efield.append(100E11*FullDataSet.Efield[i][0])
    fig = plt.plot(FullDataSet.Time, xpos)
    fig = plt.plot(FullDataSet.Time, efield)
    plt.show()


def RadiusPlot():
    radlist = []
    for i in range(len(FullDataSet.position)):
        radius = np.linalg.norm(FullDataSet.position[i])
        radlist.append(radius)
    plt.plot(FullDataSet.Time, radlist)
    plt.show()

def EnergyPlot():
    Energylist = []
    for i in range(len(FullDataSet.velocity)):
        Energy = 0.5*9.11E-31*(np.linalg.norm(FullDataSet.velocity[i]))**2
        Energylist.append(Energy)
    plt.plot(FullDataSet.Time, Energylist)
    plt.show()

PositionPlot()
VelocityPlot()
EnergyPlot()