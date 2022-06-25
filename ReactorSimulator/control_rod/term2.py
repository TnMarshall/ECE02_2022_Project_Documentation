import sys
import math
from pyXSteam.XSteam import XSteam as xs

control_rod_rad = float(sys.argv[1])
Core_Radius = float(sys.argv[2])
d_control_rod = float(sys.argv[3])#from leakage rate ^
table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
t = 0.116+math.log(Core_Radius/2.405/control_rod_rad)+d_control_rod/control_rod_rad
print(t)