from lib2to3.pgen2.pgen import generate_grammar
import pygame

class Intersection:
    def __init__(self, position, vstreet, hstreet) -> None:
        self.position = position
        self.vstreet = vstreet
        self.hstreet = hstreet
        self.traffic_light = {(0, 1): True, (0, -1): True, (1, 0): True, (-1, 0): True} #True = open

    def update(self, simulation) -> None:
        self.draw(simulation.screen)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, (0, 255, 0), self.position, 5)

    def __str__(self) -> str:
        return f'Intersection: {self.position}, {self.vstreet}, {self.hstreet}'