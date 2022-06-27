import random
import pygame

class Car:
    def __init__(self, position, direction: tuple) -> None:
        """_summary_

        Args:
            position (tuple[int]): current (x, y) position of the car. (0, 0) is the upper left corner of the screen
            direction (tuple[int]): describes the direction which the car is going to.
                It can be up (0, -1), down (0, 1), left (-1, 0) or right (1, 0).
        """
        self.set_speed()
        self.position = position
        self.direction = direction
        pass

    def set_speed(self) -> None:
        self.speed = random.randint(1, 15)

    def change_street(self, intersection):
        pass

    def move(self, street) -> None:
        # add the direction * speed to the current position
        new_position = (
            self.position[0] + self.direction[0] * self.speed,
            self.position[1] + self.direction[1] * self.speed
        )

        

        self.position = new_position

    def update(self, simulation):
        self.move(simulation.streets)
        self.draw(simulation.screen)

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, 10)

            

