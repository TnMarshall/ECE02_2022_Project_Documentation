from myDeriv import myDeriv
from myEval import myEval

def newton(val, poly, tol):
    eps = 1
    x = val
    deriv = myDeriv(poly)

    #MAX_ITER = 10000
    #iter = 0

    while (eps > tol): # and not (iter > MAX_ITER):
        temp = x - (myEval(poly, x) / myEval(deriv, x))
        eps = abs(x-temp)
        x = temp
        #iter += 1
    
    return x