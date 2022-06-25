from pyXSteam.XSteam import XSteam as xs
import sys

Pressure = float(sys.argv[1]) # Pressure(bar)
table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
print((table.rho_pt(Pressure, 20)/1000))