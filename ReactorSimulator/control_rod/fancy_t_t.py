import sys

fancytt = float(sys.argv[1])#B25, normally its value is 27
p20 = float(sys.argv[2])
p = float(sys.argv[3])#from leakage rate ^
t = fancytt *((p20/p)**2)
print(t)