class simp:
    def __init__(self, low, high, steps, func):
        self.lowerLimit = low ; self.upperLimit = high 
        self.nOS = steps
        self.func = func
        
        self.step_size = (high - low)/steps

    def result13(self):
        I = 0
        J = 0
        func = self.func
        A = self.lowerLimit
        B = self.upperLimit

        for i in range(1, self.nOS, 2):
            I += func(self.lowerLimit + i*self.step_size)
        
        for i in range(2,self.nOS,2):
            J += func(self.lowerLimit + i*self.step_size)
        
        return self.step_size*(func(A) + 4e0*I + 2e0*J + func(B))/3e0
    
    def result38(self):
        I = 0
        J = 0
        K = 0
        A = self.lowerLimit
        B = self.upperLimit
        func = self.func
        
        for i in range(1, self.nOS, 3):
            I += func(self.lowerLimit + i*self.step_size)
        
        for i in range(2,self.nOS,3):
            J += func(self.lowerLimit + i*self.step_size)
            
        for i in range(2,self.nOS,3):
            K += func(self.lowerLimit + i*self.step_size)
            
        return 3e0*self.step_size*(func(A) + 3e0*I + 3e0*J + 2e0*K + func(B))/8e0