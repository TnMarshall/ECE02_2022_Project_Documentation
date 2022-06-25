from pyXSteam.XSteam import XSteam as xs
import sys


core_radius = float(sys.argv[1])
d = float(sys.argv[2]) #this is d_small, same folder, H20

R = core_radius+d
print(R)