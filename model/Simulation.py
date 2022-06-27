import random
import time

import pygame

from model.Intersection import Intersection
from model.Street import Street
from GLOBAL_VARIABLES import *
from utils import get_intersection


class Simulation:
    """Simulates a scenario of the traffic of a city"""

    def __init__(self, nbr_streets = 20) -> None:
        self.streets = [Street(10) for i in range(nbr_streets)]

        # calculate the intersections
        self.intersections = []
        for i in range(len(self.streets)):
            for j in range(i + 1, len(self.streets)):
                intersection = get_intersection(self.streets[i], self.streets[j])
                if intersection:
                    self.intersections.append(intersection)
                    self.streets[i].intersections.append(intersection)
                    self.streets[j].intersections.append(intersection)

    def run(self):
        
        # calculate execution time
        start_time = time.time()

        # initialize pygame
        pygame.init()
        running = True

        # fill the screen with white
        self.screen = pygame.display.set_mode((1000, 1000))

        # main loop
        while running:

            self.screen.fill((255, 255, 255))

            for street in self.streets:
                street.update(self.screen)

            for intersection in self.intersections:
                intersection.update(self.screen)
                
            # update the display
            pygame.display.update()

            # check for end conditions
            if time.time() - start_time > MAX_EXECUTION_TIME:
                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # wait FPS seconds
            FramePerSec.tick(FPS)


        return time.time() - start_time
