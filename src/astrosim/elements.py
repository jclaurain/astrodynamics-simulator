import numpy as np

def initialV(rMag,mu1,i,orbitType = "elliptical",e=None,mu2=None):    #i in radians
    if orbitType == "elliptical":
        if e == None:
            raise ValueError("e must have a value for an elliptical orbit")
        else:
            if mu2 == None:
                a = rMag/(1-e)      #rMag is periapsis radius for elliptical case
                vMag = np.sqrt(mu1*((2/rMag)-(1/a)))
                v0 = np.array([0.0,
                                vMag*np.cos(i),
                                vMag*np.sin(i)])
            else:  #no inclination yet
                rp1 = mu2/(mu1+mu2)*rMag  #both bodies at periapsis (pi out of phase)
                rp2 = mu1/(mu1+mu2)*rMag
                a1 = rp1/(1-e)
                a2 = rp2/(1-e)
                v1Mag = np.sqrt((mu1+mu2)*((2/rp1)-(1/a1)))
                v2Mag = np.sqrt((mu1+mu2)*((2/rp2)-(1/a2)))
                v0 = np.array([0.0,v1Mag,0.0,0.0,-v2Mag,0.0])
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