import numpy as np
from piecewise_const import piecewise_const

# Setup

## Chao and Attard
# Chao and Attard is used to match compare performance with results from the paper.
lambdaArray = [0.0127, 0.0317, 0.115, 0.311, 1.4, 3.87]; L = 0.00002
beta = [0.000266, 0.001491, 0.001316, 0.002849, 0.000896,0.000182]
beta_sum = 0.007

test_rho_003 = np.array([[1,  0.1, 1, 2.2098], [10, 0.1, 1, 8.0192], [20, 0.01,1, 2.8297*10**1]])

test_rho_007 = np.array([[0.01, 0.0001, 4, 4.5088], [0.5,  0.0001, 4, 5.3459*10**3],[2,    0.001,  4, 2.0591*10**11]])

test_rho_008 = np.array([[0.01, 0.0001, 5, 6.0229], [0.5,  0.0001, 5, 1.4104*10**3], [0.5,  0.001,  5, 6.1634*10**23]])

m = len(lambdaArray)
init_cond = np.zeros((m+1,1)) #ARRAYSHAPE
init_cond[0,0] = 1
for i in range(1, m+1):
    init_cond[i,0] = beta[i-1] / (L* lambdaArray[i-1])
rval = np.transpose([0,0,0,0,0,0,0])

# Run all cases

for i in range(3):
    target = test_rho_003[i,0]
    h = test_rho_003[i,1]
    rho_case = test_rho_003[i,2]
    z = piecewise_const(lambdaArray, beta, beta_sum, L, target, h , rho_case , 1, init_cond, rval)
    fileName = "./zResults/pythonZ_{rho}_{iter}.csv".format(rho = 0.003, iter = i)
    np.savetxt(fileName, z, delimiter=',')

    target = test_rho_007[i,0]
    h = test_rho_007[i,1]
    rho_case = test_rho_007[i,2]
    z = piecewise_const(lambdaArray, beta, beta_sum, L, target, h , rho_case , 1, init_cond, rval)
    fileName = "./zResults/pythonZ_{rho}_{iter}.csv".format(rho = 0.007, iter = i)
    np.savetxt(fileName, z, delimiter=',')

    target = test_rho_008[i,0]
    h = test_rho_008[i,1]
    rho_case = test_rho_008[i,2]
    z = piecewise_const(lambdaArray, beta, beta_sum, L, target, h , rho_case , 1, init_cond, rval)
    fileName = "./zResults/pythonZ_{rho}_{iter}.csv".format(rho = 0.008, iter = i)
    np.savetxt(fileName, z, delimiter=',')