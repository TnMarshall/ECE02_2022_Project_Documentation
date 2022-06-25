import numpy as np
from copy import deepcopy
from newton import newton
from myHorner import myHorner

def rootfinder(coeff_0, init, tol):
    """This is a simple wrapper function that takes an coefficent vector
    and uses Newtons method to find all of the real roots of said poly
    The function takes advantage of Horners method to deflate the poly
    at each step to expedite computation. The argument init is a
    vector of initial values that are used in Newtons method."""
    coeff = deepcopy(coeff_0)
    deg = len(coeff) - 1
    result = np.zeros((deg, 1))
    counter = 0

    while (deg > 1):
        result[counter] = newton(init[counter], coeff, tol)
        coeff = myHorner(coeff, result[counter], deg)
        deg = deg - 1
        counter += 1

    result[counter] = -coeff[0]/coeff[1]
    return result