def rho(case_num, beta_sum, t):
    """This function represents the time-dependent reactivity function
    for the point kinetics equation. We will use the argument "case"
    to determine what type of reactivity we have in question. If an
    unknown case is encountered the function returns 0.
    case_num = 1 : Step reactivity of rho = 0.003
    case_num = 2 : Step reactivity of rho = 0.0055
    case_num = 3 : Ramp reactivity"""

    if case_num == 1:
        result = 0.003
    if case_num == 2:
        result = 0.0055
    if case_num == 3:
        result = 0.1*beta_sum*t
    if case_num == 4:
        result = 0.007
    if case_num == 5:
        result = 0.008
    
    return result