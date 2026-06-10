import numpy as np
import logging

logger = logging.getLogger(__name__)

class Track:
    
    def __init__(self,grid):
        self.grid = np.array(grid)
        
    def is_valid_position(self, x, y):
        if x < 0 or x >= self.grid.shape[1] or y < 0 or y >= self.grid.shape[0]:
            logger.debug(f"Position ({y}, {x}) is out of bounds.")
            return False
        return True

    def is_wall(self, x, y):
        if not self.is_valid_position(x, y):
            return False
        if self.grid[y, x] == 1:
            logger.debug(f"Position ({y}, {x}) is a wall.")
            return True
        return False