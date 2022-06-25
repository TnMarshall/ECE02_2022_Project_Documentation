import sys

ltmod = float(sys.argv[1])
p20 = float(sys.argv[2])
p = float(sys.argv[3])#from leakage rate ^
Tc_ave = float(sys.argv[4])
t = ltmod**2*(p20/p)^2*((Tc_ave+273)/293)**0.97
print(t)