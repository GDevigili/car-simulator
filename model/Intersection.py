from lib2to3.pgen2.pgen import generate_grammar
import pygame

from utils import generate_random_position


class Intersection:
    def __init__(self) -> None:
        self.position = generate_random_position()
