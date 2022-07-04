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
        for direction in self.traffic_light:
            position = (self.position[0] - 6*direction[0], self.position[1] - 6*direction[1])
            if self.traffic_light[direction]:
                pygame.draw.circle(screen, (0, 255, 0), position, 2)
            else:
                pygame.draw.circle(screen, (255, 0, 0), position, 2)


    def __str__(self) -> str:
        return f'Intersection: {self.position}, {self.vstreet}, {self.hstreet}'