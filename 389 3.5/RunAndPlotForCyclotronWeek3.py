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


electron = RelativisticChargedParticle(np.array([0,0,-10]),np.array([6.282,0,0]),np.array([0,0,0]),'electron', 9.11E-31, 9.11E-31, 1.6E-19)
MyElectricField = OscillatingField(np.array([10E-10,0,0]),0, 0)
MyMagneticField = Field(np.array([0,3.577E-11,0]))

def lorentzforce(q,e,v,b):
    force = (q*e)+(q*(np.cross(v,b)))
    return(force)

def movechargedparticlethroughEMField(chargedobject,efield,mfield,timestep,duration,radius):
    velocitydata = [[],[],[]]
    positiondata=[[],[],[]]
    speeddata = []
    t = 0
    timelist = []
    for _ in np.arange(0,duration,timestep):
        t += timestep
        #chargedobject.gammaupdate()
        #chargedobject.relativemassupdate()
        mfield.field[1] = (chargedobject.mass*np.linalg.norm(chargedobject.velocity))/(chargedobject.charge*radius)
        cyclofreq = np.linalg.norm(chargedobject.velocity)/radius
        efield.freq = cyclofreq
        efield.update(t)
        if np.linalg.norm(chargedobject.position[0]) < (0.05*2*np.pi*radius):
            chargedobject.acceleration = (lorentzforce(chargedobject.charge,efield.field,chargedobject.velocity,mfield.field))/chargedobject.mass
        else:
            chargedobject.acceleration = (lorentzforce(chargedobject.charge,0,chargedobject.velocity,mfield.field))/chargedobject.mass
        chargedobject.update(timestep)
        for i in range(0,3,1):
            positiondata[i].append(chargedobject.position[i])
            velocitydata[i].append(chargedobject.velocity[i])
        timelist.append(t)
        speeddata.append(np.linalg.norm(chargedobject.velocity))
    positiondataset = {'Time': timelist, 'xposition': positiondata[0], 'yposition': positiondata[1], 'zposition': positiondata[2]}
    velocitydataset = {'Time': timelist, 'xvelocity': velocitydata[0], 'yvelocity': velocitydata[1], 'zvelocity': velocitydata[2]}
    pdf = pd.DataFrame(data = positiondataset) 
    vdf = pd.DataFrame(data = velocitydataset)
    plt.plot(vdf['Time'],speeddata)
    #fig = plt.axes(projection = '3d', xlabel = 'x', ylabel = 'y', zlabel = 'z')
    #fig.plot3D(pdf['xposition'],pdf['yposition'],pdf['zposition'])
    plt.show()



movechargedparticlethroughEMField(electron,MyElectricField,MyMagneticField,0.0001,20,10)




