import numpy as np
from astrosim.constants import muEarth,radiusEarth
from astrosim.propagator import propagateOrbit,rVFromSol
from astrosim.plotting import animateOrbit
from astrosim.elements import initialV, orbitalPeriod

def main():
    h = 500 #km
    e = 0.06
    r0 = np.array([radiusEarth+h,0,0])
    rMag = np.linalg.norm(r0)
    v0 = initialV(rMag,muEarth,0,"elliptical",e)

    state0 = np.concatenate((r0,v0))

    T = orbitalPeriod(rMag,muEarth,"elliptical",e)

    solution = propagateOrbit(state0,T,muEarth,500)

    r,v,t = rVFromSol(solution)

    animateOrbit(r,t,radiusEarth,semiMinor=None,resolution=250,speed=5000.0)

if __name__ == "__main__":
    main()