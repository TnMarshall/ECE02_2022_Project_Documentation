import sys


mf = float(sys.argv[1])
cf = float(sys.argv[2])
power = float(sys.argv[3])
tou = float(sys.argv[4])
tft = float(sys.argv[5])
Tc = float(sys.argv[6])
pr = (power/ (mf * cf)) - (tft-Tc)/tou
print(pr)