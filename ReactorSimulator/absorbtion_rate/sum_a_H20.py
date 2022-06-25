import sys

h20n = float(sys.argv[1])
hsig = float(sys.argv[2])
osig = float(sys.argv[3])
sig_h20 = h20n * (2*hsig+osig)*(10**(-24))
print(sig_h20)