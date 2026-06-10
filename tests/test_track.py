import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pytest
import numpy as np
from src.tracks import Track

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
    

