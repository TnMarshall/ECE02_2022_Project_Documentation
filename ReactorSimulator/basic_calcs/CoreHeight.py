import sys
from math import pi
import math

Core_Volume = float(sys.argv[1])
HDR = float(sys.argv[2])

h = math.pow(Core_Volume*(math.pow(HDR, 2))*4/pi,(1/3))*100

print(h) #centimeters