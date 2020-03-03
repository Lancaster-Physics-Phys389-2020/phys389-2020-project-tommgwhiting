import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ClassFileWeek3 import RelativisticChargedParticle
from ClassFileWeek3 import ChargedParticle
from ClassFileWeek3 import Field
from ClassFileWeek3 import OscillatingField


electron = RelativisticChargedParticle(np.array([0,0,0]),np.array([6.282,0,0]),np.array([0,0,0]),'electron', 9.11E-31, 9.11E-31, 1.6E-19)
MyElectricField = OscillatingField(np.array([10E-10,0,0]),0)
MyMagneticField = Field(np.array([0,3.577E-11,0]))

def lorentzforce(q,e,v,b):
    force = (q*e)+(q*(np.cross(v,b)))
    return(force)

def movechargedparticlethroughEMField(chargedobject,efield,mfield,timestep,duration):
    velocitydata = []
    positiondata=[]
    timelist = []
    t = 0
    efield.freq = (chargedobject.charge*mfield.field[1])/chargedobject.mass
    for _ in np.arange(0,duration,timestep):
        t += timestep
        efield.update(t)
        if np.abs(chargedobject.position[0]) < 0.05:
            chargedobject.acceleration = (lorentzforce(chargedobject.charge,efield.field,chargedobject.velocity,mfield.field))/chargedobject.mass
        else: 
            chargedobject.acceleration = (lorentzforce(chargedobject.charge,0,chargedobject.velocity,mfield.field))/chargedobject.mass
        chargedobject.update(timestep)
        velocitydata.append(np.array(chargedobject.velocity))
        positiondata.append(np.array(chargedobject.position))
        timelist.append(t)
    completedataset = {'Time': timelist, 'position': positiondata, 'velocity': velocitydata}
    df = pd.DataFrame(data = completedataset)
    df.to_pickle(r'h:/3rd Year Python/389 3.0/cyclotrondata')
    return(chargedobject)


movechargedparticlethroughEMField(electron,MyElectricField,MyMagneticField,0.00001,5)




