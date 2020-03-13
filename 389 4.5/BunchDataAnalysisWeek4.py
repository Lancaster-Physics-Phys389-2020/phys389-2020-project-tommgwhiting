import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

FullDataSet = pd.read_pickle(r'h:/3rd Year Python/389 4.0/cyclotrondata') 

def PositionPlot():
    XPosPart1 = []
    XPosPart2 = []
    XPosPart3 = []
    ZPosPart1 = []
    ZPosPart2 = []
    ZPosPart3 = []
    for i in range(len(FullDataSet.Particle1)):
        XPosPart1.append(FullDataSet.Particle1[i].position[0])
        ZPosPart1.append(FullDataSet.Particle1[i].position[2])
        XPosPart2.append(FullDataSet.Particle2[i].position[0])
        ZPosPart2.append(FullDataSet.Particle2[i].position[2])
        XPosPart3.append(FullDataSet.Particle3[i].position[0])
        ZPosPart3.append(FullDataSet.Particle3[i].position[2])
    plt.plot(XPosPart1, ZPosPart1, '-', label = 'First')
    plt.plot(XPosPart2, ZPosPart2, '-', label = 'Second')
    plt.plot(XPosPart3, ZPosPart3, '-', label = 'Third')
    plt.xlabel('X Position (m)')
    plt.ylabel('Z Position (m)') 
    plt.show()

def VelocityPlot():
    speedlist = [[],[],[]]
    for i in range(len(FullDataSet.Particle1)):
        speed1 = np.linalg.norm(FullDataSet.Particle1[i].velocity)
        speed2 = np.linalg.norm(FullDataSet.Particle2[i].velocity)
        speed3 = np.linalg.norm(FullDataSet.Particle3[i].velocity)
        speedlist[0].append(speed1)
        speedlist[1].append(speed2)
        speedlist[2].append(speed3)
    plt.plot(FullDataSet.Time, speedlist[0])
    plt.plot(FullDataSet.Time, speedlist[1])
    plt.plot(FullDataSet.Time, speedlist[2])
    plt.xlabel('Time')
    plt.ylabel('Speed of Particle (ms-1)')
    plt.show()

def FindKineticEnergyinEV(mass,velocity):
    ke = (0.5*mass*velocity*velocity)/constants.elementary_charge
    return(ke)

def EnergyPlot():
    Energylist = [[],[],[]]
    for i in range(len(FullDataSet.Particle1)):
        energy1 = FindKineticEnergyinEV(FullDataSet.Particle1[i].mass,np.linalg.norm(FullDataSet.Particle1[i].velocity))
        energy2 = FindKineticEnergyinEV(FullDataSet.Particle2[i].mass,np.linalg.norm(FullDataSet.Particle2[i].velocity))
        energy3 = FindKineticEnergyinEV(FullDataSet.Particle3[i].mass,np.linalg.norm(FullDataSet.Particle3[i].velocity))
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
    devlist = []
    for i in range(len(FullDataSet.Particle1)):
        averageposition = np.mean([FullDataSet.Particle1[i].position,FullDataSet.Particle2[i].position,FullDataSet.Particle3[i].position])
        spreadfromavg = [np.linalg.norm(averageposition - FullDataSet.Particle1[i].position),
                         np.linalg.norm(averageposition - FullDataSet.Particle2[i].position),
                         np.linalg.norm(averageposition - FullDataSet.Particle3[i].position)]
        deviation = np.std(spreadfromavg)
        devlist.append(deviation)
    plt.plot(FullDataSet.Time, devlist)
    plt.xlabel('Time(s)')
    plt.ylabel(' Spread Deviation (m)')
    plt.show()

# EnergyPlot()
# PositionPlot()
# VelocityPlot()
# SpreadPlot()


print(FullDataSet.BunchData[0])