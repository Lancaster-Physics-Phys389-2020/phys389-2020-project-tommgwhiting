import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FullDataSet = pd.read_pickle(r'h:/3rd Year Python/389 4.0/cyclotrondata')

def PositionPlot():
    xpos = [[],[],[]]
    ypos = [[],[],[]]
    zpos = [[],[],[]]
    for i in range(0,len(FullDataSet.position1),4):
        xpos[0].append(FullDataSet.position1[i][0])
        ypos[0].append(FullDataSet.position1[i][1])
        zpos[0].append(FullDataSet.position1[i][2])
        xpos[1].append(FullDataSet.position2[i][0])
        ypos[1].append(FullDataSet.position2[i][1])
        zpos[1].append(FullDataSet.position2[i][2])
        xpos[2].append(FullDataSet.position3[i][0])
        ypos[2].append(FullDataSet.position3[i][1])
        zpos[2].append(FullDataSet.position3[i][2])
    plt.plot(xpos[0],zpos[0], '-', label = 'First')
    plt.plot(xpos[1],zpos[1], '-', label = 'Second')
    plt.plot(xpos[2],zpos[2], '-', label = 'Third')
    plt.xlabel('X Position (m)')
    plt.ylabel('Z Position (m)')
    plt.show()

def VelocityPlot():
    speedlist = [[],[],[]]
    for i in range(len(FullDataSet.velocity1)):
        speed1 = np.linalg.norm(FullDataSet.velocity1[i])
        speed2 = np.linalg.norm(FullDataSet.velocity2[i])
        speed3 = np.linalg.norm(FullDataSet.velocity3[i])
        speedlist[0].append(speed1)
        speedlist[1].append(speed2)
        speedlist[2].append(speed3)
    plt.plot(FullDataSet.Time, speedlist[0])
    plt.plot(FullDataSet.Time, speedlist[1])
    plt.plot(FullDataSet.Time, speedlist[2])
    plt.xlabel('Time')
    plt.ylabel('Speed of Particle (ms-1)')
    plt.show()

def EnergyPlot():
    Energylist = [[],[],[]]
    for i in range(len(FullDataSet.velocity1)):
        energy1 = (0.5*9.11E-31*(np.linalg.norm(FullDataSet.velocity1[i]))**2)/1.6E-19
        energy2 = (0.5*9.11E-31*(np.linalg.norm(FullDataSet.velocity2[i]))**2)/1.6E-19
        energy3 = (0.5*9.11E-31*(np.linalg.norm(FullDataSet.velocity3[i]))**2)/1.6E-19
        Energylist[0].append(energy1)
        Energylist[1].append(energy2)
        Energylist[2].append(energy3)
    plt.plot(FullDataSet.Time, Energylist[0])
    plt.plot(FullDataSet.Time, Energylist[1])
    plt.plot(FullDataSet.Time, Energylist[2])
    plt.xlabel('Time(s)')
    plt.ylabel('Enegy of Particles (eV)')
    plt.show()

def SpreadPlot():
    SpreadList = []
    for i in range(len(FullDataSet.velocity1)):
        spread = np.linalg.norm(FullDataSet.position2[i]) - np.linalg.norm(FullDataSet.position1[i])
        SpreadList.append(spread)
    plt.plot(FullDataSet.Time, SpreadList)
    plt.xlabel('Time(s)')
    plt.ylabel('Spread of Particles (m)')
    plt.show()

#PositionPlot()
#VelocityPlot()
EnergyPlot()
#SpreadPlot()
