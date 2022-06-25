from pyXSteam.XSteam import XSteam as xs
import sys
import math

ltmod20 = float(sys.argv[1])
Pressure = float(sys.argv[2]) # Pressure(bar)
Average_Coolant_Temperature = float(sys.argv[3]) #average coolant temperature

table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
ans = ltmod20*table.rho_pt(Pressure,20)/table.rho_pt(Pressure,Average_Coolant_Temperature)*math.sqrt(((Average_Coolant_Temperature+273)/293)**0.97)
print(ans)