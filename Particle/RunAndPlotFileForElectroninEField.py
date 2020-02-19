import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from FieldandParticleClasses import ChargedParticle
from FieldandParticleClasses import ElectricField
from FieldandParticleClasses import MagneticField


electron = ChargedParticle([0,0,0],np.array([2,0,0]),[0,0,0],'electron',2,1)
MyElectricField = ElectricField(np.array([0,0,0]),np.array([0,0,0]))
MyMagneticField = MagneticField(np.array([0,2,0]),np.array([0,0,0]),np.array([0,2,0]))

def lorentzforce(q,e,v,b):
    force = (q*e)+(q*(np.cross(v,b)))
    return(force)

def movechargedparticlethroughEMField(chargedobject,efield,mfield,timestep,duration):
    positiondata=[[],[],[]]
    t = 0
    timelist = []
    for _ in np.arange(0,duration,timestep):
        t += timestep
        chargedobject.acceleration = (lorentzforce(chargedobject.charge,efield.electric,chargedobject.velocity,mfield.magnetic))/chargedobject.mass
        chargedobject.update(timestep)
        efield.update(timestep)
        mfield.oscillate(t,1)
        for i in range(0,3,1):
            positiondata[i].append(chargedobject.position[i])
        timelist.append(t)
    dataset = {'Time': timelist, 'xposition': positiondata[0], 'yposition': positiondata[1], 'zposition': positiondata[2]}
    df = pd.DataFrame(data = dataset) 
    fig = plt.axes(projection = '3d', xlabel = 'x', ylabel = 'y', zlabel = 'z')
    fig.plot3D(df['xposition'],df['yposition'],df['zposition'])
    plt.show()


movechargedparticlethroughEMField(electron,MyElectricField,MyMagneticField,0.01,50)



