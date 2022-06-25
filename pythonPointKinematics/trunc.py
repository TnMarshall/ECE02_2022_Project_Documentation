import numpy as np

def trunc(var, t):
    """This is a simple helper method that removes the ith element
    from the vector var."""

    m = len(var)
    flag = 0   
    temp = np.zeros((m-1, 1)) # TODO this worries me

    for i in range(m):
        if (i != t) and (flag == 0):
            temp[i] = var[i]
        
        if (i != t) and (flag == 1):
            temp[i-1] = var[i]
        
        if i ==t:
            flag = 1
    
    #return np.transpose(temp)
    return temp