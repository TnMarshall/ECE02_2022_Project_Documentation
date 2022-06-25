import sys

power = float(sys.argv[1])
cv = float(sys.argv[2])#core volume
ERJ = float(sys.argv[3])
pr = float(sys.argv[4])  #production rate
npf = float(sys.argv[5]) # neutrons per fission

peak = 3.64*power/cv/ERJ/(pr/npf)
print(peak)

