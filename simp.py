from simps import simp

import math
import numpy as np
import matplotlib.pyplot as plt

# Tested with a complex one
# It takes long time to solve!! Requires more development
def Jn(theta, args):
    x, n = args
    A = x*math.cos(theta)
    B = (math.sin(theta)) ** (2.00*n + 1.00)
    C = (x ** n)/( (2.00 ** (n+1))*math.factorial(n) )
    final = C*math.cos(A)*B
    return final

def F(r): return 1.00 - r*r

def overall_integrand(r, arg):
    u = arg[0]
    return F(r)*r*simp(0, math.pi, 100, Jn, u*r, 0).result13()
    
u = np.linspace(0,25,501)
Y = []
for i in u:
    overall =  simp(0,1,100,overall_integrand, i).result13()
    Y.append(overall)


plt.plot(u,Y)
plt.title("Radiation Vs. Distance")
plt.xlabel("Distance")
plt.ylabel("Radiation")
plt.axis([0,25,0,0.25])
plt.grid(True)
plt.show()



''' # Tested for Multiple Arguments
def F(phi, args):
    thetaM = args[0]
    A = math.sin(thetaM/2.00)*math.sin(thetaM/2.00)
    B = math.sin(phi)*math.sin(phi)
    C = 1.000 - A*B
    D = 1.000/C
    final = math.sqrt(D)
    return final
    
phi = np.linspace(0, math.pi/2.00, 1001)
a = 4.0*math.sqrt(0.0253)
for p in phi:
    result = simp(0, math.pi/2.00, 120, F, p).result38()  #result13 for Simpson's 1/3 rule
    print("{}\t{}".format(p, a*result))
'''
    
''' # Tested for Single Argument
def F(x):
    return x*x*x
    
#             Lower Limit,    Upper Limit, Number of Iterations, Functions
result = simp(2, 3, 120, F).result38()  #result13 for Simpson's 1/3 rule
print(result)
'''

'''
x = np.linspace(0,25.00,1001)    
y = []
for i in x:
    obj = [simp(0, math.pi, 120, Jn, i, j).result13() for j in range(5)]
    y.append(obj)

#plt.plot(x,y)
#plt.show()
'''



