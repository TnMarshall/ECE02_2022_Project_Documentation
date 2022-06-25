import os
import numpy as np

target = 100
stepSize = 1
rho_case = 1
n = 10
numInternalSteps = int(target/stepSize)

for i in range(1,numInternalSteps+1):
    target = i
    command1 = "python3 pcrun_perf_testing.py {target} {stepSize} {rho_case} > output.csv".format(target = target, stepSize = stepSize, rho_case = rho_case)
    commandLoop = "python3 pcrun_perf_testing.py {target} {stepSize} {rho_case} >> output.csv".format(target = target, stepSize = stepSize, rho_case = rho_case)

    os.system(command1)
    for i in range(n-1):
        os.system(commandLoop)

    data = np.genfromtxt('output.csv', delimiter=',')

    avgRuntime = np.sum(data)/n

    numInternalSteps = int(target/stepSize)
    print(numInternalSteps)
    print(avgRuntime)
    # out1 = "Number of Internal Steps: {numIter}".format(numIter = numInternalSteps)
    # out2 = "Number of Iterations Used for Average: {numIter}".format(numIter = n)
    # out3 = "Average Run Time: {avgRun}".format(avgRun = avgRuntime)
    avgRep = "echo {avgTime} >> timingData.csv".format(avgTime = avgRuntime)
    os.system(avgRep)

# print(out1)
# print(out2)
# print(out3)