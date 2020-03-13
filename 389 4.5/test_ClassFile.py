import numpy as np 
import math
from scipy import constants
from pytest import approx

from ClassFileWeek4 import Field
from ClassFileWeek4 import OscillatingField
from ClassFileWeek4 import Particle
from ClassFileWeek4 import ChargedParticle
from ClassFileWeek4 import RelativisticChargedParticle

def test_Field():
    genericfield = Field(np.array([1,2,3]))
    assert np.all(genericfield.field == np.array([1,2,3]))
    genericfield.field = np.array([4,5,6])
    assert np.all(genericfield.field == np.array([4,5,6]))


def test_OscillatingField():
    waveyfield = OscillatingField(np.array([2,2,2]),(2*np.pi))
    waveyfield.update(0.25)
    assert waveyfield.field[0] == approx(0)
    assert waveyfield.field[1] == approx(0)
    assert waveyfield.field[2] == approx(0)

def test_Particle():
    testparticle = Particle(np.array([0,0,0]),np.array([0,0,0]),np.array([1,1,1]),'Test',1)
    testparticle.update(2)
    assert np.all(testparticle.velocity == np.array([2,2,2]))
    assert np.all(testparticle.position == np.array([4,4,4]))

def test_ChargedParticle():
    testchargedparticle = ChargedParticle(np.array([0,0,0]),np.array([0,0,0]),np.array([1,1,1]),'Test',1,constants.elementary_charge)
    print(testchargedparticle.charge)
    assert (testchargedparticle.charge) == approx(1.6E-19)

def test_RelativisticChargedParticle():
    samplerelativisticchargedparticle = RelativisticChargedParticle(np.array([0,0,0]),np.array([0,0,0]),np.array([1,1,1]),'Test',1,1,constants.elementary_charge,1)
    samplerelativisticchargedparticle.velocity = np.array([0.99*constants.speed_of_light,0,0])
    samplerelativisticchargedparticle.gammaupdate()
    assert samplerelativisticchargedparticle.gamma == 7.088812050083393

