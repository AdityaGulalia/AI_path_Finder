import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.simulation import Simulation

class RandomAgent:
    def __init__(self, simulation):
        self.simulation = simulation

    def choose_action(self):
        import random
        return random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])

    def run(self, steps=10):
        for _ in range(steps):
            action = self.choose_action()
            self.simulation.step(action)
            rendered_grid = self.simulation.render_human()
            print("\n".join("".join(row) for row in rendered_grid))