import numpy as np

def ev2(lambdaArray, L, beta, evals):
    """This is a simple function that calculates the eigenvectors using the
    appropriate forms"""

    m = len(lambdaArray) + 1

    evects = np.zeros((m, m))

    for i in range(m):
        for j in range(m):
            if i == 0:
                evects[i,j] = 1
            else:
                mu = beta[i-1]/L
                evects[i,j] = mu / (lambdaArray[i-1] + evals[j])
    
    return evects