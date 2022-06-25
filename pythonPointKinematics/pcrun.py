import numpy as np
from piecewise_const import piecewise_const
import time
# pcrun.py
# This is a dummy script to run the piecewise constant function tic
## Chao and Attard
#lambdaArray = [0.0127, 0.0317, 0.115, 0.311, 1.4, 3.87]; L = 0.00002
#beta = [0.000266, 0.001491, 0.001316, 0.002849, 0.000896,0.000182]
#beta_sum = 0.007

# Norbrega Thermal Reactor
lambdaArray = np.array([0.0127, 0.0317, 0.115, 0.311, 1.40, 3.87])
L = 5e-4
beta = np.array([2.850e-4, 1.5975e-3, 1.410e-3, 3.0525e-3, 9.600e-4, 1.950e-4])
beta_sum = 0.00750

## Norbreaga Fast Reactor
#  lambda = [0.0129, 0.0311, 0.134, 0.331, 1.26, 3.21]
#  L = 1e-7
#  beta = [1.672e-4, 1.232e-3, 9.504e-4, 1.443e-3, 5.434e-4, 1.540e-4]
#  beta_sum = 0.00440

## Two Group
# lambda = [.077]
# L = [.0001]
# beta = [.0079]
# beta_sum = 0.0079

# A short code for computing the initial equilibrium conditions
m = len(lambdaArray)
init_cond = np.zeros((m+1,1)) #ARRAYSHAPE
init_cond[0,0] = 1
for i in range(1, m+1):
    init_cond[i,0] = beta[i-1] / (L* lambdaArray[i-1])
rval = np.transpose([0,0,0,0,0,0,0])
z = piecewise_const(lambdaArray, beta, beta_sum, L, 1, .1 , 1 , 1, init_cond, rval)
np.savetxt("pythonZ.csv", z, delimiter=',')