import sys

n235 = float(sys.argv[1])
sigma_U = float(sys.argv[2]) #B16
f = n235 * sigma_U * (10**(-24))
print(f)