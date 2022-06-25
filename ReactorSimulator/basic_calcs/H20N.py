from pyXSteam.XSteam import XSteam as xs
import sys

Pressure = float(sys.argv[1]) # Pressure(bar)
Tc_ave = float(sys.argv[2]) # average coolant temp
table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
print((table.rho_pt(Pressure, Tc_ave)*6.022*(10**23)/18/1000000*1000))