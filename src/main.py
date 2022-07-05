import sys
sys.path.append('..')
from threading import Thread
from multiprocessing import Process

from model.Simulation import Simulation
from GLOBAL_VARIABLES import n_processes
import random


if __name__ == '__main__':
    random.seed(10) # seed: 10
    running = True

    while(running):
        try:
            simulation = Process(target=Simulation(n_processes=n_processes, nbr_streets=30).run())
            simulation.start()
            simulation.join()

            del simulation
            # Simulation(n_processes=n_processes, nbr_streets=30).run()
        except KeyboardInterrupt:
            running = False
            print('\nSimulation stopped')
            break
