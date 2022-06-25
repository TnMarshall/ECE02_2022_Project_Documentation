from pyXSteam.XSteam import XSteam as xs
import sys
import math
from scipy import special

ltmod20 = float(sys.argv[1]) #ltmod20
Pressure = float(sys.argv[2]) # Pressure(bar)
Average_Coolant_Temperature = float(sys.argv[3]) #average coolant temperature
Fuel_Radius = float(sys.argv[4])
LTFuel = float(sys.argv[5])
LatticePitch = float(sys.argv[6])
sigmaATH= float(sys.argv[7])
sigmATO= float(sys.argv[8])
coreHeight = float(sys.argv[9])
coreVolume = float(sys.argv[10])
EnrichmentFraction = float(sys.argv[11])
sigmaA235 = float(sys.argv[12])
sigmaA238 = float(sys.argv[13])
b = LatticePitch/(math.sqrt(math.pi))
Nfuel = 2.3427*(10**22) #might need this and MFR replaced
x = Fuel_Radius/LTFuel
table = xs(xs.UNIT_SYSTEM_MKS) #m/kg/sec/°C/bar/W
ltmod = ltmod20*table.rho_pt(Pressure,20)/table.rho_pt(Pressure,Average_Coolant_Temperature)*math.sqrt(((Average_Coolant_Temperature+273)/293)**0.97)
y = Fuel_Radius/ltmod
z = b/ltmod
F = x*(special.i0(x))/2/(special.i1(x))

term1 = ((z**2)-(y**2))/2/y
term2 = special.i0(y)*special.k1(z) + special.k0(y)*special.i1(z)
term3 = special.i1(z)*special.k1(y) - special.k1(z)*special.i1(y)
E = term1 * term2 / term3

sumAM = table.rho_pt(Pressure,Average_Coolant_Temperature)/1000*6.022*(10**23)/18*(2*sigmaATH+sigmATO)*10**-24
sumAF = (EnrichmentFraction*Nfuel*sigmaA235+(1-EnrichmentFraction)*Nfuel*sigmaA238)*(10**-24)
MFR = 2
smallF = sumAM/sumAF*MFR*F+E
answer = 1/smallF
'''
print("E: " + str(E))
print("F: " + str(F))
print("AF: " +str(sumAF))
print("AM: " +str(sumAM))



print(smallF)
'''
print(answer)
