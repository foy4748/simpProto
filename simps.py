class simp:
    def __init__(self, low, high, steps, func, *args):
        self.lowerLimit = low ; self.upperLimit = high 
        self.nOS = steps
        self.func = func
        self.step_size = (high - low)/steps
        try:
            self.args = args
        except:
            pass
        

    def result13(self):
        I = 0
        J = 0
        func = self.func
        A = self.lowerLimit
        B = self.upperLimit
        
        try:
            for i in range(1, self.nOS, 2):
                I += func(self.lowerLimit + i*self.step_size, self.args)
            
            for i in range(2,self.nOS,2):
                J += func(self.lowerLimit + i*self.step_size, self.args)
            
            result = self.step_size*(func(A,self.args) + 4e0*I + 2e0*J + func(B,self.args))/3e0
        except:
            for i in range(1, self.nOS, 2):
                I += func(self.lowerLimit + i*self.step_size)
            
            for i in range(2,self.nOS,2):
                J += func(self.lowerLimit + i*self.step_size)
            
            result = self.step_size*(func(A) + 4e0*I + 2e0*J + func(B))/3e0
        
        return result
    
    def result38(self):
        I = 0
        J = 0
        K = 0
        func = self.func
        A = self.lowerLimit
        B = self.upperLimit
        
        try:
            for i in range(1, self.nOS, 3):
                I += func(self.lowerLimit + i*self.step_size, self.args)
            
            for i in range(2,self.nOS,3):
                J += func(self.lowerLimit + i*self.step_size, self.args)
            
            for i in range(3,self.nOS,3):
                K += func(self.lowerLimit + i*self.step_size, self.args)
            result = 3e0*self.step_size*(func(A,self.args) + 3e0*I + 3e0*J + 2e0*K + func(B,self.args))/8e0
        except:
            for i in range(1, self.nOS, 3):
                I += func(self.lowerLimit + i*self.step_size)
            
            for i in range(2,self.nOS,3):
                J += func(self.lowerLimit + i*self.step_size)
            
            for i in range(3,self.nOS,3):
                K += func(self.lowerLimit + i*self.step_size)
            result = 3e0*self.step_size*(func(A) + 3e0*I + 3e0*J + 2e0*K + func(B))/8e0
        
        return result

