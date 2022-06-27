import pygame
from utils import generate_random_position, euclidean_distance
from GLOBAL_VARIABLES import MIN_STREET_DISTANCE

class Street:

    def __init__(self, max_car_capacity: int):
        self.points = ((0, 0), (0, 0))

        while euclidean_distance(self.points[0], self.points[1]) < MIN_STREET_DISTANCE:
            self.points = (
                generate_random_position(),
                generate_random_position()
            )

    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), self.points[0], self.points[1])

