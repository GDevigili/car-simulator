import sys
sys.path.append('..')
from threading import Thread

from model.Simulation import Simulation
import random


if __name__ == '__main__':
    random.seed(10) # seed: 10
    while(True):
        x = Thread(target=Simulation(30).run())
        # sim = Simulation(30)
        # sim.run()
