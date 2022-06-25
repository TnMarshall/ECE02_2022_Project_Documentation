import sys

smqav = float(sys.argv[1]) #E20
smsigma = float(sys.argv[2])
sum_a_B = smqav * smsigma * (10**(-24))

print(sum_a_B)
