import sys

p_rod = float(sys.agv[1])# from control rod
p_no_rod = float(sys.agv[1])
p = p_no_rod - p_rod

print(p)