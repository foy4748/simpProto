from simps import simp

import math
import numpy as np


def F(phi, args):
    thetaM = args[0]
    A = math.sin(thetaM/2.00)*math.sin(thetaM/2.00)
    B = math.sin(phi)*math.sin(phi)
    C = 1.000 - A*B
    D = 1.000/C
    final = math.sqrt(D)
    return final
'''
def F(x):
    return x*x*x
    

#             Lower Limit,    Upper Limit, Number of Iterations, Functions
result = simp(2, 3, 120, F).result38()  #result13 for Simpson's 1/3 rule
print(result)
'''


phi = np.linspace(0, math.pi/2.00, 1001)

a = 4.0*math.sqrt(0.0253)
for p in phi:
    result = simp(0, math.pi/2.00, 120, F, p).result38()  #result13 for Simpson's 1/3 rule
    print("{}\t{}".format(p, a*result))
