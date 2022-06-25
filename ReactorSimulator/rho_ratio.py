from pyXSteam.XSteam import XSteam
import sys
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)

p = 2000 / 14.504 # psia to bar
t = float(sys.argv[1])

rho_ratio = steamTable.rho_pt(p,20)/steamTable.rho_pt(p,t)
print(rho_ratio)