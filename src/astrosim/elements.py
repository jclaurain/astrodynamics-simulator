import numpy as np

def initialV(rMag,mu,i,orbitType = "elliptical",e=None):    #i in radians
    if orbitType == "elliptical":
        if e == None:
            raise ValueError("e must have a value for an elliptical orbit")
        else:
            a = rMag/(1-e)      #rMag is periapsis radius for elliptical case
            vMag = np.sqrt(mu*((2/rMag)-(1/a)))
            v0 = np.array([0.0,
                               vMag*np.cos(i),
                               vMag*np.sin(i)])
    else:
        raise ValueError("orbitType must be elliptical")
    return v0

def orbitalPeriod(rMag,mu,orbitType="elliptical",e=None):
    if orbitType == "elliptical":
        if e == None:
            raise ValueError("e must have a value for an elliptical orbit")
        else:
            a = rMag/(1-e)      #rMag is periapsis radius for elliptical orbit
            T = 2*np.pi*np.sqrt(a**3/mu)
    else:
            raise ValueError("orbitType must be circular or elliptical")
    return T