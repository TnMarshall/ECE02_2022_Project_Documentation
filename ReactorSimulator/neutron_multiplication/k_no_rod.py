import sys

pr = float(sys.argv[1]) # production rate
sum_a = float(sys.argv[2]) #sum all absorbtion rate
leakage = float(sys.argv[3]) #leakage from leakage rate
k = pr /(sum_a + leakage)
print(k)