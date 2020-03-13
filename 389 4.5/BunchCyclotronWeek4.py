import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy

from ClassFileWeek4 import RelativisticChargedParticle
from ClassFileWeek4 import ChargedParticle
from ClassFileWeek4 import Field
from ClassFileWeek4 import OscillatingField
from BunchClass import BunchOfParticles

def movebunchthroughEMField(particlelist,efield,mfield,duration):
    timelist = []
    avgposlist = []
    energyspreadlist = []
    avgspdlist = []
    avgenergylist = []
    t = 0
    counter = 0
    efield.freq = (particlelist[0].charge*mfield.field[1])/particlelist[0].mass
    averagepos = np.array([0,0,0])
    while t < duration:
        BunchClass = BunchOfParticles(particlelist)
        timestep = 1E-3/np.linalg.norm(BunchClass.listofparticles[0].velocity)
        counter += 1
        t += timestep
        efield.update(t)
        averagepos = BunchClass.averageposition()
        BunchClass.bunchgammaupdate()
        BunchClass.bunchrelativisticmassupdate()
        if averagepos[0] < 0.05:
            BunchClass.accelerationupdate(efield.field,mfield.field)
        else: 
            BunchClass.accelerationupdate(0,mfield.field)
        for i in range(len(BunchClass.listofparticles)):
            BunchClass.listofparticles[i].update(timestep)
        averagespd = np.linalg.norm(BunchClass.averagevelocity())
        if (counter%15) == 0:
            timelist.append(t)
            avgposlist.append(averagepos)
            avgspdlist.append(averagespd)
            energyspread = BunchClass.spreadenergy()
            energyspreadlist.append(energyspread)
            Energy = []
            for i in range(len(BunchClass.listofparticles)):
                Energy.append((BunchClass.listofparticles[i].relativeenergy())/constants.elementary_charge)
            avgenergy = np.mean(Energy)
            avgenergylist.append(avgenergy)
        if np.linalg.norm(averagepos) > 2:
            break
        if counter%1000 == 0:
            print ('Program is %s Percent Complete'%(np.round((np.linalg.norm(averagepos)/2)*100)))

    dataset = {'Time' : timelist, 'AveragePosition' : avgposlist, 'AverageSpeed' : avgspdlist, 'EnergySpread' : energyspreadlist, 'AverageEnergy': avgenergylist}
    df = pd.DataFrame(data = dataset)
    df.to_pickle(r'h:/3rd Year Python/389 4.0/cyclotrondata')

BunchList = []

for i in range(13):
    BunchList.append(RelativisticChargedParticle(np.array([0,0,0]),np.array([(3E5+(i*1E2)),0,0]),np.array([0,0,0]),'electron%s'%(i+1),constants.electron_mass,constants.electron_mass,constants.elementary_charge, 1))


MyElectricField = OscillatingField(np.array([4,0,0]),0,-(np.pi/8))
MyMagneticField = Field(np.array([0,3E-2,0]))


movebunchthroughEMField(BunchList,MyElectricField,MyMagneticField,5E-5)

# TestBunch = BunchOfParticles(BunchList)
# print(TestBunch.averageposition())


