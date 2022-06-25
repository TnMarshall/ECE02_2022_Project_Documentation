from math import pi
import sys

rtilde = float(sys.argv[1])
htilde= float(sys.argv[2])
B = (2.405/rtilde)**2+(pi/rtilde/htilde)**2
print(B)