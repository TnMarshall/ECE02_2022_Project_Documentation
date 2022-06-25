import sys

mt2 = float(sys.argv[1])
Core_Radius = float(sys.argv[2])
b2 = float(sys.argv[3])#from leakage rate ^

t = 7.43*mt2/(1+b2*mt2)/(Core_Radius)**2
print(t)