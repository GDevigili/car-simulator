import pygame
import random

from utils import generate_random_position, euclidean_distance
from GLOBAL_VARIABLES import MIN_STREET_DISTANCE, MAX_MAP_X, MAX_MAP_Y


class Street:

    def __init__(self, max_car_capacity: int):
        self.points = [(0, 0), (0, 0)]

        self.orientation = random.choice(['h', 'v'])

        if self.orientation == 'h':
            self.points[0] = (
                random.randint(1, MAX_MAP_X - MIN_STREET_DISTANCE - 1),
                random.randint(1, MAX_MAP_Y)
            )
            self.points[1] = (
                random.randint(self.points[0][0] + MIN_STREET_DISTANCE, MAX_MAP_X),
                self.points[0][1]
            )
        else:
            self.points[0] = (
                random.randint(1, MAX_MAP_X),
                random.randint(1, MAX_MAP_Y - MIN_STREET_DISTANCE - 1)
            )
            self.points[1] = (
                self.points[0][0],
                random.randint(self.points[0][1] + MIN_STREET_DISTANCE, MAX_MAP_Y)
            )

        # while euclidean_distance(self.points[0], self.points[1]) < MIN_STREET_DISTANCE:
        #     self.points = (
        #         generate_random_position(),
        #         generate_random_position()
        #     )

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), self.points[0], self.points[1])
