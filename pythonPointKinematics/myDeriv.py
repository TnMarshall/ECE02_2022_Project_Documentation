import numpy as np

def myDeriv(coeff):
    """A simple function that calculates the derivitive
    coefficient vector for a given polynomial."""

    deg = len(coeff)

    if deg != 1:
        result = np.zeros((deg-1, 1))

        for i in range(deg-1):
            result[i] = coeff[i+1] * (i+1)
    else:
        result = 0

    return result