import sys

D = float(sys.argv[1]) #from leakage rate, big D
c_rod_rad= float(sys.argv[2])# control rod radius
sum_t_h2o = float(sys.argv[3])


d = 2.13*D*(c_rod_rad*sum_t_h2o+0.9354)/(c_rod_rad*sum_t_h2o+0.5098)

print(d)