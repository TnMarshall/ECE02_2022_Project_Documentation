import numpy as np

def swap(arg):
    """This simple function takes the 1st element of arg and puts it in the
    mth place of the resultant vector, and puts the 2nd in the m-lst, ,and
    so on. . ."""

    m = len(arg)
    res = np.zeros((1, m))

    for i in range(m):
        res[m-i+1] = arg[i]
    
    return res