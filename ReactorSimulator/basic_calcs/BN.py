import sys

boron_Mass = float(sys.argv[1])#grams
Core_Volume = float(sys.argv[2])
n = boron_Mass/Core_Volume/1000000*6.022*10**22
#print(n)
print(n)