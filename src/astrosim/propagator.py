from scipy.integrate import solve_ivp
from astrosim.dynamics import twoBodyEOM
import numpy as np

def propagateOrbit(state0,tSpan,mu,points):
    tEval = np.linspace(0,tSpan,points)

    solution = solve_ivp(twoBodyEOM,
                         (0,tSpan),
                         state0,
                         args=(mu,),
                         t_eval=tEval,
                         rtol=1e-9,
                         atol=1e-9)
    return solution


def rVFromSol(solution):
    t = solution.t
    r = solution.y[0:3,:]
    v = solution.y[3:6,:]
    return r,v,t