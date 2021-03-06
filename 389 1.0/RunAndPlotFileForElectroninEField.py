import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from FieldandParticleClasses import ChargedParticle
from FieldandParticleClasses import Field
from FieldandParticleClasses import OscillatingField


electron = ChargedParticle([0,0,0],np.array([0,1,0]),[0,0,0],'electron',1,2)
MyElectricField = OscillatingField(np.array([0,2,0]),1)
MyMagneticField = OscillatingField(np.array([0,0,0]),1)

def lorentzforce(q,e,v,b):
    force = (q*e)+(q*(np.cross(v,b)))
    return(force)

def movechargedparticlethroughEMField(chargedobject,efield,mfield,timestep,duration):
    velocitydata = [[],[],[]]
    positiondata=[[],[],[]]
    t = 0
    timelist = []
    for _ in np.arange(0,duration,timestep):
        t += timestep
        if efield.field[1] > 0:
            chargedobject.acceleration = (lorentzforce(chargedobject.charge,efield.field,chargedobject.velocity,mfield.field))/chargedobject.mass
        chargedobject.update(timestep)
        efield.update(t)
        for i in range(0,3,1):
            positiondata[i].append(chargedobject.position[i])
            velocitydata[i].append(chargedobject.velocity[i])
        timelist.append(t)
    positiondataset = {'Time': timelist, 'xposition': positiondata[0], 'yposition': positiondata[1], 'zposition': positiondata[2]}
    velocitydataset = {'Time': timelist, 'xvelocity': velocitydata[0], 'yvelocity': velocitydata[1], 'zvelocity': velocitydata[2]}
    pdf = pd.DataFrame(data = positiondataset) 
    vdf = pd.DataFrame(data = velocitydataset)
    plt.plot(vdf['Time'],vdf['yvelocity'])
    #fig = plt.axes(projection = '3d', xlabel = 'x', ylabel = 'y', zlabel = 'z')
    #fig.plot3D(pdf['xposition'],pdf['yposition'],pdf['zposition'])
    plt.show()


movechargedparticlethroughEMField(electron,MyElectricField,MyMagneticField,0.0001,10)



