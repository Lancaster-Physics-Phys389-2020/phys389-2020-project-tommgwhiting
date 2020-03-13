import numpy as np 
import math
from scipy import constants

class Field:
    def __init__(self, FieldStrength = np.array([0,0,0]), dtype = float):
        self.field = np.array(FieldStrength, dtype = float)

    def __repr__(self):
        return 'Field Strength : %s' %(self.field)


class OscillatingField(Field):
    def __init__(self, FieldStrength = np.array([0,0,0], dtype = float), OscillationFrequency = 0, Phase = 0):
        super().__init__(FieldStrength = FieldStrength)
        self.freq = OscillationFrequency
        self.amp = FieldStrength
        self.phase = Phase

    def __repr__(self):
        return 'Field Amplitude : %s, Oscillation Frequency of Field: %s'%(self.amp, self.freq)

    def update(self, currenttime):
        self.field = self.amp*np.cos((currenttime*self.freq)+self.phase)


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

class RelativisticChargedParticle(ChargedParticle):

    def __init__(self, Position = np.array([0,0,0], dtype = float), Velocity = np.array([0,0,0],dtype = float),
                 Acceleration = np.array([0,0,0], dtype = float), Name = 'electron', RelativeMass = constants.electron_mass, RestMass = constants.electron_mass,
                 Charge = constants.elementary_charge, Gamma = 1):

                 super().__init__(Position = Position, Velocity = Velocity, Acceleration = Acceleration, Name = Name,
                 Charge = Charge)
                 self.restmass = RestMass
                 self.gamma = 1

    def __repr__(self):
        return 'Relativistic Charged Particle : %s, Mass: %s, Charge: %s, Position: %s, Velocity: %s, Acceleration: %s, Gamma Factor: %s'%(self.Name, self.mass, 
        self.charge, self.position, self.velocity, self.acceleration, self.gamma)

    def gammaupdate(self):
        speed = np.linalg.norm(self.velocity)
        beta = speed/constants.speed_of_light
        self.gamma = 1/np.sqrt((1-beta*beta))
        return self.gamma

    def relativemassupdate(self):
        self.mass = self.gamma*self.restmass
        return self.mass

    def relativeenergy(self):
        EinsteinEnergy = self.mass*constants.speed_of_light*constants.speed_of_light
        return EinsteinEnergy