import numpy as np

class Car:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def propose_move(self, dx, dy):
        return self.x + dx, self.y + dy 

    def set_position(self, x, y):
        self.x = x
        self.y = y
        
        