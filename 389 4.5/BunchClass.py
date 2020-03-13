import numpy as np 
import math
from scipy import constants
import itertools as it 


from ClassFileWeek4 import RelativisticChargedParticle
from ClassFileWeek4 import Field

def lorentzforce(q,e,v,b):
    force = (q*e)+(q*(np.cross(v,b)))
    return(force)


class BunchOfParticles:

    def __init__(self, Particles):
        self.listofparticles = Particles

    def __repr__(self):
        for i in range(len(self.listofparticles)+1):
            return('Name : %s, Rest Mass : %s, Current Mass: %s, Position : %s, Velocity : %s, Accleration : %s, Gamma : %s'
            %(self.listofparticles[i].Name, self.listofparticles[i].restmass, self.listofparticles[i].mass, self.listofparticles[i].position,
             self.listofparticles[i].velocity, self.listofparticles[i].acceleration, self.listofparticles[i].gamma))

    def accelerationupdate(self, electricfield, magneticfield):
        for i in range(len(self.listofparticles)):
            self.listofparticles[i].acceleration = lorentzforce(self.listofparticles[i].charge,electricfield,self.listofparticles[i].velocity,magneticfield)/self.listofparticles[i].mass

    def averageposition(self):
        listofpositions = []
        for i in range(len(self.listofparticles)):
            listofpositions.append(self.listofparticles[i].position)
        avgpos = np.mean(listofpositions, axis = 0)
        return(avgpos)

    def averagevelocity(self):
        listofvelocities = []
        for i in range(len(self.listofparticles)):
            listofvelocities.append(self.listofparticles[i].velocity)
        avgvel = np.mean(listofvelocities, axis = 0)
        return(avgvel)

    def spreadposition(self):
        listofseperations = []
        for particle1, particle2 in it.combinations(self.listofparticles, 2):
            seperation = np.linalg.norm(particle1.position - particle2.position)
            listofseperations.append(seperation)
        spread = np.mean(listofseperations)
        return(spread)

    def spreadenergy(self):
        listofenergies = []
        for particle1, particle2 in it.combinations(self.listofparticles, 2):
            energyseperation = particle1.relativeenergy() - particle2.relativeenergy()
            listofenergies.append(energyseperation)
        energyspread = np.std(listofenergies)
        return(energyspread)

    def bunchgammaupdate(self):
        for i in range(len(self.listofparticles)):
            self.listofparticles[i].gammaupdate()
        
    def bunchrelativisticmassupdate(self):
        for i in range(len(self.listofparticles)):
            self.listofparticles[i].relativemassupdate()




