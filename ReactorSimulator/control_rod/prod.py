import sys
import math

pw = float(sys.argv[1])
CRIF = float(sys.argv[2]) #B10

prod = pw*(CRIF-1/2/math.pi*math.sin(2*math.pi*CRIF))
#print(prod)
print(prod)