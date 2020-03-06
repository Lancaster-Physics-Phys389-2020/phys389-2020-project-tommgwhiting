import numpy as np 
import math
from scipy import constants

from ClassFileWeek4 import RelativisticChargedParticle
from ClassFileWeek4 import Field


class BunchOfParticles:

    def __init__(self, Particles):
        self.listofparticles = Particles

    def __repr__(self):
        for i in range(len(self.listofparticles)):
            particle = self.listofparticles[i]
            return(('Name : %s, Rest Mass : %s, Current Mass: %s, Position : %s, Velocity : %s, Accleration : %s, Gamma : %s'
            %(particle.Name, particle.restmass, particle.mass, particle.position, particle.velocity, particle.acceleration, particle.gamma)))








