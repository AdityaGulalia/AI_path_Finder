import numpy as np
import pytest
from src.simulation import Simulation
from src.cars import Car

@pytest.fixture()
def default_simulation():
    return Simulation(2, 2)

def test_car_pos_initialization(default_simulation):
    assert default_simulation.car.x == 2
    assert default_simulation.car.y == 2
    
def test_move_to_new_position(default_simulation):
    dx, dy = 1, 0
    expected_x = default_simulation.car.x + dx
    expected_y = default_simulation.car.y + dy
    
    assert default_simulation.new_position(dx, dy) == True  
    assert default_simulation.car.x == expected_x
    assert default_simulation.car.y == expected_y
    
def test_move_to_wall(default_simulation):
    dx, dy = 0, -4
    
    initial_pos_x = default_simulation.car.x
    initial_pos_y = default_simulation.car.y
    
    assert default_simulation.new_position(dx, dy) == False
    
    assert default_simulation.car.x == initial_pos_x
    assert default_simulation.car.y == initial_pos_y
    
def test_step_function_map_action_to_movement(default_simulation):
    initial_x = default_simulation.car.x
    initial_y = default_simulation.car.y
    
    default_simulation.step('UP')
    
    assert default_simulation.car.x == initial_x
    assert default_simulation.car.y == initial_y - 1

def test_step_function_invalid_action(default_simulation):
    initial_x = default_simulation.car.x
    initial_y = default_simulation.car.y
    
    result = default_simulation.step('INVALID_ACTION')
    
    assert result == False
    assert default_simulation.car.x == initial_x
    assert default_simulation.car.y == initial_y
    
def test_render_function(default_simulation):
    expected_rendered_grid = [[1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 1],
                            [1, 0, 2, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1]]
    rendered_grid = default_simulation.render()
    
    assert np.array_equal(rendered_grid, expected_rendered_grid)
    
def test_render_human(default_simulation):
    expected_rendered_grid = [['#', '#', '#', '#', '#'],
                            ['#', '.', '.', '.', '#'],
                            ['#', '.', 'C', '.', '#'],
                            ['#', '.', '.', '.', '#'],
                            ['#', '#', '#', '#', '#']]
    rendered_grid = default_simulation.render_human()
    
    assert np.array_equal(rendered_grid, expected_rendered_grid)