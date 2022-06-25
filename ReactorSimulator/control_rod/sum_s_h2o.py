import sys

h2on = float(sys.argv[1])
sigmaH = float(sys.argv[2])
sigmaO = float(sys.argv[3])
sum_s_h2o = h2on*(10**(-24))*(2*sigmaH+sigmaO)
print(sum_s_h2o)