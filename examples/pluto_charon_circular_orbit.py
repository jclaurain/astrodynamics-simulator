import numpy as np
from astrosim.elements import initialV
from astrosim.constants import muPluto, muCharon

def main():
    rMag = 19600 #km
    v0 = initialV(muPluto,0.0,"eliptical",0.0,muCharon)
    r0 = np.array([-(muCharon/(muCharon+muPluto))*rMag,0.0,0.0,(muPluto/(muCharon+muPluto))*rMag,0.0,0.0])
    state0 = np.concatenate(r0,v0)