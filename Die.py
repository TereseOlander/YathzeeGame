import numpy as np

# Class that creates a die
class dice():
    def __init__(self,sides=7):
        self.sides=sides
    
    def roll(self): 
        value = np.random.randint(1,self.sides)
        return value
    