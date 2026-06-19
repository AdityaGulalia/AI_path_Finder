import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.random_agents import RandomAgent
from src.simulation import Simulation
from utilis.logger import setup_logger

def main():
    try:
        setup_logger("simulation_log")
        sim = Simulation(2, 2)
        agent = RandomAgent(sim)
        agent.run(steps=10)

    except IndexError as error:
        return error

if __name__ == "__main__":
    main()