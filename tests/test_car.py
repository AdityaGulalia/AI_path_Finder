import pytest
import numpy as np
from src.simulation import Simulation
from src.cars import Car

@pytest.fixture
def default_car():
    return Car(1, 1)

def test_car_position(default_car):
    assert default_car.x == 1
    assert default_car.y == 1
    
def test_propose_move(default_car):
    dx, dy = 3, 0
    expected_x = default_car.x + dx
    expected_y = default_car.y + dy
    
    assert default_car.propose_move(dx, dy) == (expected_x, expected_y)
    