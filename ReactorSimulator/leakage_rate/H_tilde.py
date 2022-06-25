from pyXSteam.XSteam import XSteam as xs
import sys


core_height = float(sys.argv[1])
d = float(sys.argv[2]) #this is d_small, same folder, H20

H = core_height+2*d
print(H)