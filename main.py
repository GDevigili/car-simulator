import sys
sys.path.append('..')

from model.Simulation import Simulation
import random


if __name__ == '__main__':
    random.seed(10)
    sim = Simulation(20)
    sim.run()
