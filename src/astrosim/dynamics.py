import numpy as np

def twoBodyAcceleration(r,mu):
    rMag = np.linalg.norm(r)
    a = -mu*(r/rMag**3)
    return a

def twoBodyEOM(t,state,mu):
    r = state[0:3]
    v = state[3:6]

    a = twoBodyAcceleration(r,mu)

    stateDerivative = np.concatenate((v,a))

    return stateDerivative