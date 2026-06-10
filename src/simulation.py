import numpy as np
from src.tracks import Track
from src.cars import Car 
import logging

logger = logging.getLogger(__name__)

class Simulation:
    
    def __init__(self, x, y):
        self.grid = np.array([[1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1]])
        self.track = Track(self.grid)
        self.car = Car(x, y)

    def run(self, x, y):
        self.track.is_valid_position(x, y)
        self.track.is_wall(x, y)
        
    def new_position(self, dx, dy):
        
        if self.track.is_valid_position(self.car.x, self.car.y) and not self.track.is_wall(self.car.x, self.car.y):
            logger.debug(f"car moved to {self.car.x},{self.car.y}")
            self.car.move(dx, dy)
            return True
        else:
            logger.debug(" is_valid_position or is wall failed ")
            return False
