import numpy as np
from rootfinder import rootfinder
from trunc import trunc
from expand import expand

def inhour(lambdaArray, L, beta, rho, init_root):
    """This function begins by taking the arguments and converting them into
    the correct m-degree polynomial inorder to take advantage of the given
    method of finding the roots of said polynomial."""

    m = len(lambdaArray)
    sum = np.zeros((m, 1))
    coeff = expand(lambdaArray)
    coeff_2 = np.zeros((m+2, 1))

    for i in range(1, m+1):
        coeff_2[i] = rho*coeff[i] - L*coeff[i-1]

    coeff_2[0] = rho*coeff[0]
    coeff_2[m+1] = -L * coeff[m]

    for i in range(m):
        temp_lambda = trunc(lambdaArray, i)
        temp = beta[i] * expand(temp_lambda)
        sum = temp + sum # does this perform array addition correctly? (probably yes)

    sum = -1*sum
    res = np.zeros((m+2, 1))

    for i in range(m):
        res[i+1] = coeff_2[i+1] + sum[i]
        # Check if this matrix math is accurate

    res[0] = coeff_2[0]
    res[m+1] = coeff_2[m+1]
    e_vals = rootfinder(res, init_root, 0.00001)

    return e_vals