from Library import *
import math
import numpy as np

N = 100000
randomNo1 = LCG(2,N,487,0,18745)


def function(x):
    return np.exp(-x**2)
# integral without importance sampling
result = MonteCarlo(function,randomNo1,N,0, 1)
print("Monte Carlo integration without importance sampling: ",result)

def Integral(N):
    total = 0
    rand = LCG(3, N, 472, 0, 16745)
    for i in range(N):
        X = -math.log(1 - (math.exp(1)-1)/math.exp(1)*rand[i])
        total += (math.exp(1)-1)/math.exp(1)*math.exp(-X**2)/math.exp(-X)
    return total/N

resultIS = Integral(N)
print("Monte Carlo integration with importance sampling: ",resultIS)
# Monte Carlo integration without importance sampling:  0.7465376001227405
# Monte Carlo integration with importance sampling:  0.7468376497354626