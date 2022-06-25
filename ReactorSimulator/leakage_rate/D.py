from pyXSteam.XSteam import XSteam as xs
import sys

D20 = 0.16
p20 = float(sys.argv[1])
p = float(sys.argv[2])
Tc_ave = float(sys.argv[3])# average coolant temp
#table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
D = D20 * (p20/p)*((Tc_ave+273)/293)**(0.47)
#print(D)
print(D)