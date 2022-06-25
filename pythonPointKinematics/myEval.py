def myEval(coeff, x):
    """Evaluates the polynomial expressed as coeff at the value x."""
    deg = len(coeff)
    sum = coeff[0]

    if deg != 1:
        for i in range(1, deg):
            sum = sum + coeff[i] * x**i
            
    return sum