import sys
sys.path.append('..')

from model.Simulation import Simulation


if __name__ == '__main__':
    sim = Simulation()
    sim.run()
