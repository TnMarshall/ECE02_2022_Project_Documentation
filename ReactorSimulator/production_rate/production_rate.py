import sys

npf = float(sys.argv[1])
n235 = float(sys.argv[2])
usigma = float(sys.argv[3])
pr = npf*n235*usigma*(10**(-24))
print(pr)