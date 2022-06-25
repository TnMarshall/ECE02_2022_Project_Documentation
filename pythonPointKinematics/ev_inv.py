import numpy as np

def ev_inv(lambdaArray, L, beta, evals):
    """This function returns the inverse of the matrix of eigenvalues
     based on some computations provieded in Aboanber and Nahla."""

    mu = []

    m = len(lambdaArray) + 1

    for i in range(m-1):
        mu.append(beta[i]/L)

    norm_fact = np.zeros((m, 1))

    for k in range(m):
        sum = 0
        for i in range(m-1):
            temp = round(mu[i]*lambdaArray[i],15) #TODO determine the best way to correct for the .####9999999 repeating issue
            temp2 = round(lambdaArray[i] + evals[k][0],13)**2
            temp3 = round(temp/temp2,15)
            sum = sum+temp3
        
        norm_fact[k] = 1/(sum+1)

    result = np.zeros((m, m))

    for i in range(m):
        for j in  range(m):
            if i == 0:
                result[i,j] = 1*norm_fact[j]
            else:
                result[i,j] = (lambdaArray[i-1] / (lambdaArray[i-1] + evals[j])) * norm_fact[j]

    
    return np.transpose(result)
