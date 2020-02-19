import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ElectricField:

    def __init__(self, EFieldStrength = np.array([0,0,0]), EFieldGrowthRate = np.array([0,0,0]), dtype = float):
        self.electric = np.array(EFieldStrength, dtype = float)
        self.growthrate = np.array(EFieldGrowthRate, dtype = float)

    def __repr__(self):
        return 'Field Strength: %s' %(self.electric)

    def update(self, deltaT):
        self.electric += self.growthrate*deltaT

class MagneticField:
    def __init__(self, MFieldStrength = np.array([0,0,0]), MFieldGrowthRate = np.array([0,0,0]), MfieldAmp = np.array([0,0,0]), dtype = float):
        self.magnetic = np.array(MFieldStrength, dtype = float)
        self.growthrate = np.array(MFieldGrowthRate, dtype = float)
        self.amp = np.array(MfieldAmp, dtype = float)
    def __repr__(self):
        return 'Field Strength: %s' %(self.magnetic)

    def update(self, deltaT):
        self.magnetic += self.growthrate*deltaT

    def oscillate(self, currentime, oscillationperiod):
        self.magnetic = self.amp*np.cos((currentime/oscillationperiod)*2*np.pi)

class Particle:

    def __init__(self, Position=np.array([0,0,0], dtype=float), Velocity=np.array([0,0,0], dtype=float), Acceleration=np.array([0,0,0], dtype=float), Name='Ball', Mass=1.0):
        self.Name = Name
        self.position = np.array(Position,dtype=float)
        self.velocity = np.array(Velocity,dtype=float)
        self.acceleration = np.array(Acceleration,dtype=float)
        self.mass = Mass

    def __repr__(self):
        return 'Particle: {0}, Mass: {1:12.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}'.format(self.Name,self.mass,self.position, self.velocity,self.acceleration)

    def KineticEnergy(self):
        return 0.5*self.mass*np.vdot(self.velocity,self.velocity)
  
    def momentum(self):
        return self.mass*np.array(self.velocity,dtype=float)

    def update(self, deltaT):
        self.velocity +=  self.acceleration*deltaT
        self.position +=  self.velocity*deltaT


class ChargedParticle(Particle):

    def __init__(self, Position = np.array([0,0,0], dtype = float), Velocity = np.array([0,0,0],dtype = float),
                 Acceleration = np.array([0,0,0], dtype = float), Name = 'electron', Mass = constants.electron_mass,
                 Charge = constants.elementary_charge):

                 super().__init__(Position = Position, Velocity = Velocity, Acceleration = Acceleration, Name = Name,
                 Mass = Mass)

                 self.charge = Charge
    
    def __repr__(self):
        return 'Charged Particle: %s, Mass: %s, Charge %s, Position: %s, Velocity: %s, Acceleration %s'%(self.Name, self.mass, self.charge, self.position, self.velocity, self.acceleration)

