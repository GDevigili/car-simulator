import random
import pygame

from utils import is_between

class Car:
    def __init__(self, position, direction: tuple, current_street) -> None:
        """_summary_

        Args:
            position (tuple[int]): current (x, y) position of the car. (0, 0) is the upper left corner of the screen
            direction (tuple[int]): describes the direction which the car is going to.
                It can be up (0, -1), down (0, 1), left (-1, 0) or right (1, 0).
        """
        self.set_speed()
        self.position = position
        self.direction = direction
        self.current_street = current_street

    def set_speed(self) -> None:
        self.speed = random.randint(1, 10)

    def change_street(self):
        # define the directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # remove the current direction
        directions.remove(self.direction)
        # get a random direction
        self.direction = random.choice(directions)
        # set a new speed
        self.set_speed()
        print(self.direction, self.speed)

    def move(self, street) -> None:
        # add the direction * speed to the current position
        new_position = (
            self.position[0] + self.direction[0] * self.speed,
            self.position[1] + self.direction[1] * self.speed
        )

        return new_position

    def check_move(self, street):
        for intersection in street.intersections:
            if intersection.position == self.position:
                self.change_street()
                self.position = self.move(street)
                return 0
            else:
                new_position = self.move(street)
                if is_between(intersection.position, self.position, new_position):
                    new_position = intersection.position
                self.position = new_position

    def update(self, simulation, current_street):
        self.check_move(current_street)
        self.draw(simulation.screen)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, 10)

            

