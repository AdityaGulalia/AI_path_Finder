import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import simulation
from utilis.logger import setup_logger

def main():
    try:
        setup_logger("simulation_log")
        sim = simulation.Simulation(1, 1)
        sim.run(1, 1)
        sim.new_position(1, 0)

    except IndexError as error:
        return error

if __name__ == "__main__":
    main()