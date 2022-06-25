import numpy as np
import math
import sys
from rho import rho
from inhour import inhour
from ev2 import ev2
from f import f
from ev_inv import ev_inv


def piecewise_const(lambdaArray, beta, beta_sum, L, target, h, rho_case, f_case, initcond):

    ## This function will calculate the solution to the point kinetics equation
    # starting at time = 0. The following is a summary of the arguments for the
    # function:
    # lambda = a vector of the decay constants for the delayed neutrons
    # beta = a vector containing the delayed-neutron fraction
    # beta_sum = the sum of all of the betas
    # L = neutron generation time
    # target = the final, target time of the function
    # h = step size
    # rho_case = this value will determine the type of time dependent
    # reactivity for the program. A full listing of these
    # various values can be found in rho.m
    # f_case = similar to "rho_case" but it determines the source term
    # to be used
    lambdaArray_f = lambdaArray#np.array(lambdaArray)
    beta_f = beta#np.array(beta)
    m_f = 6
    init_cond = np.zeros((m_f + 1, 1))  # ARRAYSHAPE

    init_cond[0, 0] = initcond[0]

    for i in range(1, m_f + 1):
        init_cond[i, 0] = initcond[i]#4#beta_f[i - 1] / (L * lambdaArray_f[i - 1])

    # Determine the number of delay groups, thereby the size of our solution 
    m = 7

    # Calculate the values of several constants that will be needed in
    # the control of the iterations as well as set up some basic matrices.
    x = init_cond 
    time = 0
    rval = np.transpose([0, 0, 0, 0, 0, 0, 0])
    f_hat = np.zeros((m,1))
    d_hat = np.zeros((m,m))
    big_d = np.zeros((m,m))
    i = 0
    iterations = target / h

    result = np.zeros((m+1,int(iterations)))
    # Begin time dependent iterations
    d=rval
    while time <= (target-h):
        time = time + h
        # Calculate the values of the reactivity and source at the midpoint
        mid_time = (time-time+h)/2
        p = rho_case#rho(rho_case, beta_sum, mid_time)
        source = f(f_case, mid_time)
        
        # Calculate the roots to the inhour equation
        d = inhour(lambdaArray_f, L, beta_f, p, d)
        
        # Calculate the eigenvectors and the inverse of the matrix
        # of eigenvectors
        Y = ev2(lambdaArray_f, L, beta_f, d)
        Y_inv = ev_inv(lambdaArray_f, L, beta_f, d)
        
        # Construct matrices for computation
        for k in range(m):   # Iterator is 0-indexed, don't use for math
            d_hat[k,k] = math.exp(d[k]*h)
            big_d[k,k] = d[k]
        
        f_hat[0] = source
        big_d_inv = np.zeros((m,m))
        
        for k in range(m):
            big_d_inv[k,k] = 1/big_d[k,k]
        
        # TODO Check matrix math
        # Compute next time step

        #TODO we ended here
        # x = (Y * d_hat * Y_inv)*(x + (Y*big_d_inv*Y_inv*f_hat)) - (Y*big_d_inv*Y_inv*f_hat)
        x = np.matmul(np.matmul(np.matmul(Y,d_hat),Y_inv),(x+np.matmul(Y,np.matmul(big_d_inv,np.matmul(Y_inv,f_hat))))) - np.matmul(np.matmul(np.matmul(Y,big_d_inv),Y_inv),f_hat)
        
        # Store results in a matrix
        for j in range(m):
            result[0,i] = time
            result[j+1,i] = x[j]
        
        #Update counters
        i = i + 1

    for_nodered = [result[1][-2], result[2][-2], result[3][-2], result[4][-2], result[5][-2], result[6][-2], result[7][-2]]
    print(for_nodered)
    #print(result)
    #return result
#convert lambda and beta into proper arrays
x = sys.argv[1]#lambda
x= x.split(',')
for a in range(0,len(x)):
    x[a] = float(x[a])

y = sys.argv[2]#beta
y = y.split(',')
for a in range(0,len(y)):
    y[a] = float(y[a])

z = sys.argv[9]#beta
z = z.split(',')
for a in range(0,len(y)):
    z[a] = float(z[a])
piecewise_const(x, y, float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7]), float(sys.argv[8]), z)