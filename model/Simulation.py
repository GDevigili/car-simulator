import random
import time

import pygame

from Intersection import Intersection
from GLOBAL_VARIABLES import *


class Simulation:
    """Simulates a scenario of the traffic of a city"""

    def __init__(self) -> None:
        self.intersections = []

        self.initialize_components()

    def initialize_components(self):
        for i in range (0, 50):
            self.intersections.append(Intersection())

    def run(self):
        
        start_time = time.time()

        pygame.init()
        running = True

        self.screen = pygame.display.set_mode((1000, 1000))

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for intersection in self.intersections:
                intersection.update(self.screen)

            pygame.display.update()
            FramePerSec.tick(FPS)

        return time.time() - start_time
