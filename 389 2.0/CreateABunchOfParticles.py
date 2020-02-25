import numpy as np 
import math
from scipy import constants
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from ClassFileWeek2 import RelativisticChargedParticle

NumberOfParticlesInBunch = 3
BunchList =[]


for i in range(NumberOfParticlesInBunch):
    Bunch.append(RelativisticChargedParticle(np.array([0,0,0]),np.array([0,2.8E8 + i*1E6,0]),np.array([0,0,0]),'electron%s'%(i+1), constants.electron_mass,
    constants.electron_mass,constants.elementary_charge))

