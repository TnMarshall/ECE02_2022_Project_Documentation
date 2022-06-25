import numpy as np

def expand(lambdaArray):
    """A simple helper function to provide the coefficients of a polynomia
    produced by raising the function (x+y) to the nth power,
    The argument, lambda is a vector of constants that are needed to
    derive the coefficients.
    Determines the number of iterations, as well as the degree
    of the polynomial in question"""

    m = len(lambdaArray)
    coeff = np.zeros((m+1, 1))

    # A temporary variable is necessary b/c the iterations that follow
    # require information from the previous iteration. . .

    temp = np.copy(coeff)

    # Must run the index to m+l b/c MATLAB uses a 1-based index

    for i in range(0, m+1):
        if i != 0:
            coeff[0,0] = temp[0,0] * lambdaArray[i-1]
            for j in range(1, m):
                coeff[j,0] = temp[j,0]*lambdaArray[i-1] + temp[j-1,0]
                if j == i-1:
                    coeff[j,0] = temp[j-1,0] + lambdaArray[i-1]
        coeff[i,0] = 1
        temp = np.copy(coeff)
    
    return coeff