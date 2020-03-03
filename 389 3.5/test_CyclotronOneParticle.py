import numpy as np
from WorkingCyclotronForSingleElectron import lorentzforce, movechargedparticlethroughEMField
from ClassFileWeek3 import RelativisticChargedParticle, Field, OscillatingField
from scipy import constants


def test_movechargedparticlethroughEMfield():
    electron = RelativisticChargedParticle(np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0]),'electron',constants.electron_mass)
    electricfield = OscillatingField(np.array([0,0,0]),0)
    magneticfield = Field(np.array([0,0,0]))
    assert movechargedparticlethroughEMField(electron,electricfield,magneticfield,100,1) == electron



def test_lorentzforce():
    a = lorentzforce(0,np.array([0,0,0]),np.array([0,0,0]),np.array([0,0,0])) 
    b = np.array([0,0,0])
    assert np.all(a == b)
    c = lorentzforce(1,np.array([1.0,1,0]),np.array([0,1,0]),np.array([1,0,0]))
    d = np.array([1,1,-1])
    assert np.all(c == d)






