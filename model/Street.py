import pygame
import random

from utils import generate_random_position, euclidean_distance
from GLOBAL_VARIABLES import MIN_STREET_DISTANCE, MAX_MAP_X, MAX_MAP_Y
from model.Intersection import Intersection


class Street:

    def __init__(self, max_car_capacity: int):

        # stores if the street is vertical(v) or horizontal(h)
        self.orientation = random.choice(['h', 'v'])

        self.intersections = []

        self.point1 = None
        self.point2 = None
        if self.orientation == 'h':
            self.point1 = (
                random.randint(1, MAX_MAP_X - MIN_STREET_DISTANCE - 1),
                random.randint(1, MAX_MAP_Y)
            )
            self.point2 = (
                random.randint(self.point1[0] + MIN_STREET_DISTANCE, MAX_MAP_X),
                self.point1[1]
            )
        else:
            self.point1 = (
                random.randint(1, MAX_MAP_X),
                random.randint(1, MAX_MAP_Y - MIN_STREET_DISTANCE - 1)
            )
            self.point2 = (
                self.point1[0],
                random.randint(self.point1[1] + MIN_STREET_DISTANCE, MAX_MAP_Y)
            )

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), self.point1, self.point2)
                
    def __str__(self) -> str:
        return f'Street: {self.orientation}, {self.point1}, {self.point2}'
                        