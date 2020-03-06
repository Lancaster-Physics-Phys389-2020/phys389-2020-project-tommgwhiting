import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ClassFileWeek4 import RelativisticChargedParticle
from ClassFileWeek4 import ChargedParticle
from ClassFileWeek4 import Field
from ClassFileWeek4 import OscillatingField
from BunchClass import BunchOfParticles


def lorentzforce(q,e,v,b):
    force = (q*e)+(q*(np.cross(v,b)))
    return(force)

def movebunchthroughEMField(particlebunch,efield,mfield,timestep,duration):
    collectionofparticles = []
    for i in range(len(particlebunch.listofparticles)):
        collectionofparticles.append(particlebunch.listofparticles[i])
    velocitydata = [[],[],[]]
    positiondata=[[],[],[]]
    timelist = []
    t = 0
    efield.freq = (collectionofparticles[0].charge*mfield.field[1])/collectionofparticles[0].mass
    for _ in np.arange(0,duration,timestep):
        t += timestep
        efield.update(t)
        for i in range(len(collectionofparticles)):
            chargedobject = collectionofparticles[i]
            if np.abs(chargedobject.position[0]) < 0.05:
                chargedobject.acceleration = (lorentzforce(chargedobject.charge,efield.field,chargedobject.velocity,mfield.field))/chargedobject.mass
            else: 
                chargedobject.acceleration = (lorentzforce(chargedobject.charge,0,chargedobject.velocity,mfield.field))/chargedobject.mass
            chargedobject.update(timestep)
            velocitydata[i].append(np.array(chargedobject.velocity))
            positiondata[i].append(np.array(chargedobject.position))
        timelist.append(t)
    
    completedataset = {'Time': timelist, 'position1': positiondata[0], 'position2': positiondata[1], 'position3': positiondata[2],
                                        'velocity1': velocitydata[0], 'velocity2': velocitydata[1], 'velocity3': velocitydata[2]}
    df = pd.DataFrame(data = completedataset)
    df.to_pickle(r'h:/3rd Year Python/389 4.0/cyclotrondata')
    return(chargedobject)

BunchList =[RelativisticChargedParticle(np.array([0,0,0]),np.array([878E7,0,0]),np.array([0,0,0]),'electron1',constants.electron_mass,constants.electron_mass,constants.elementary_charge, 1),
            RelativisticChargedParticle(np.array([0,0,0]),np.array([880E7,0,0]),np.array([0,0,0]),'electron2',constants.electron_mass,constants.electron_mass,constants.elementary_charge, 1),
            RelativisticChargedParticle(np.array([0,0,0]),np.array([882E7,0,0]),np.array([0,0,0]),'electron3',constants.electron_mass,constants.electron_mass,constants.elementary_charge, 1)]

Bunch = BunchOfParticles(BunchList)

MyElectricField = OscillatingField(np.array([1000,0,0]),0)
MyMagneticField = Field(np.array([0,1.5E-3,0]))

movebunchthroughEMField(Bunch,MyElectricField,MyMagneticField,1E-15,5E-10)




