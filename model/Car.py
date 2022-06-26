import random

from Street import Street
from Intersection import Intersection


class Car:
    def __init__(self) -> None:
        """initialize instance of car"""
        self.set_speed()
            
        pass

    def set_speed(self) -> None:
        pass

    def change_street(self, intersection: Intersection) -> Street:
        pass