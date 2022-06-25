import numpy as np

def myHorner(a, z, n):
    b = np.zeros((n+1, 1), dtype=float)

    #for i in range(n+1):
        #b[i] = 0.0

    if n>0:
        b[n-1] = a[n]

        for i in range(n):
            b[n-i-1] = a[n-i] + b[n-i]*z
        c = a[0] + b[0]*z
    else:
        raise ValueError("Zero polynomial")
    
    for i in range(n):
        a[i] = b[i]
    
    ret = np.zeros((n,1))

    for i in range(n):
        ret[i] = a[i]
    
    ret[n-1] = ret[n-1] + c

    return ret