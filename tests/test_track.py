import pytest
import numpy as np
from src.tracks import Track
from src.cars import Car
from src.simulation import Simulation

@pytest.mark.parametrize("x, y, expected", [
    (0, 0, True),  # Valid position
    (4, 4, True),  # Valid position
    (-1, 0, False), # Out of bounds
    (0, -1, False), # Out of bounds
    (5, 0, False),  # Out of bounds
    (0, 5, False)   # Out of bounds
])

def test_is_valid_position(x, y, expected):
    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    t = Track(grid)
    assert t.is_valid_position(x, y) == expected
    

@pytest.mark.parametrize("x, y, expected", [
    (1, 1, False), # Not a wall
    (0, 0, True),  # Wall
    (4, 4, True),  # Wall
    (1, 0, True),  # Wall
    (0, 1, True),  # Wall
    (2, 2, False)  # Not a wall
    ])

def test_is_wall(x, y,expected):
    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    
    t = Track(grid)
    assert t.is_wall(x,y) == expected


    