import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from src.tracks import Track
from src.cars import Car 
import logging

logger = logging.getLogger(__name__)

class Simulation:
    
    ACTIONS = {
        'UP' : (0, -1),
        'DOWN' : (0, 1),
        'LEFT' : (-1, 0),
        'RIGHT' : (1, 0)
    }
    
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
        new_x, new_y = self.car.propose_move(dx, dy)
        if self.track.is_valid_position(new_x, new_y) and not self.track.is_wall(new_x, new_y):
            self.car.set_position(new_x, new_y)
            logger.debug(f"car moved to {self.car.x},{self.car.y}")
            return True
        else:
            logger.debug(" is_valid_position or is wall failed ")
            return False

    def step(self, action):
        if action not in self.ACTIONS:
            logger.error(f"Invalid action: {action}")
            return False

        dx, dy = self.ACTIONS[action]
        
        new_x, new_y = self.car.propose_move(dx, dy)
        if self.track.is_valid_position(new_x, new_y) and not self.track.is_wall(new_x, new_y):
            self.car.set_position(new_x, new_y)
            logger.debug(f"car moved to {self.car.x},{self.car.y}")
            return True
        else:
            logger.debug(" is_valid_position or is wall failed ")
            return False
    
    def render(self):
        rendered_grid = np.copy(self.grid)
        for row in range(rendered_grid.shape[0]):
            for col in range(rendered_grid.shape[1]):
                if self.track.is_wall(col, row):
                    rendered_grid[row, col] = 1
                elif self.track.is_valid_position(col, row) and self.car.x == col and self.car.y == row:
                    rendered_grid[row, col] = 2
                elif self.track.is_valid_position(col, row):
                    rendered_grid[row, col] = 0
                else:
                    print(f"Invalid position at ({row}, {col})")
        return rendered_grid


    def render_human(self):
        rendered_grid = self.render()

        output = []

        for row in range(rendered_grid.shape[0]):
            row_string = []

            for col in range(rendered_grid.shape[1]):
                if rendered_grid[row, col] == 1:
                    row_string.append("#")
                elif rendered_grid[row, col] == 2:
                    row_string.append("C")
                else:
                    row_string.append(".")

            output.append(row_string)

        return output
