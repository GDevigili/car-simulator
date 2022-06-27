import sys
sys.path.append('..')

from model.Simulation import Simulation
import random


if __name__ == '__main__':
    random.seed(1)
    sim = Simulation(10)
    sim.run()
