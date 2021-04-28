from simps import simp

def F(x):
    return x*x*x;
    

#             Lower Limit,    Upper Limit, Number of Iterations, Functions
result = simp(2, 3, 100, F).result13()  #result13 for Simpson's 1/3 rule

print(result)

