import sys

gammaPm = float(sys.argv[1]) #E18
pr = float(sys.argv[2])#production rate
npf = float(sys.argv[3]) # neutrons per fission
smsig = float(sys.argv[4]) #B23 SM sigma
seqav = gammaPm *pr/npr/(smsig*(10**(-24)))
print(seqav)