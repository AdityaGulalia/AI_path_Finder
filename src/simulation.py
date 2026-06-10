import numpy as np
from tracks import Track
from cars import car 

class Simulation:
    
    def __init__(self):
        self.grid = np.array([[1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1]])
        self.track = Track(self.grid)
        self.car = car(0, 0)

    def run(self):
        self.track.is_valid_position(1,2)
        self.track.is_wall(1,2)
        
    
        

