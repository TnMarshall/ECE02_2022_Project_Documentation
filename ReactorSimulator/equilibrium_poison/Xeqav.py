import sys

gammal = float(sys.argv[1]) #E16
pr = float(sys.argv[2])#production rate
npf = float(sys.argv[3]) # neutrons per fission
smsig = float(sys.argv[4]) #B23 SM sigma
gammaxe = float(sys.argv[5]) #E17
flux_avg = float(sys.argv[6])
lambdax = float(sys.argv[7])
xesigma =float(sys.argv[8])
xeqav = ((gammal+gammaxe)*(pr/npf)*flux_avg) / (lambdax+(xesigma*flux_avg*(10^(-24))))
print(xeqav)

