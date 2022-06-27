from lib2to3.pgen2.pgen import generate_grammar
import pygame

from utils import generate_random_position


class Intersection:
    def __init__(self) -> None:
        self.position = generate_random_position()

    def update(self, screen) -> None:
        self.draw(screen)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, (0, 0, 0), self.position, 10)