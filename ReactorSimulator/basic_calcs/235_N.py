from pyXSteam.XSteam import XSteam as xs
import sys

Fuel_Density = float(sys.argv[1]) # Fuel_Density
#table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
n = Fuel_Density*6.022*(10**23)/235
print(n)