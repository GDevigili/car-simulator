import pygame
import random
import uuid
from random import randint

from utils import get_car_list
from GLOBAL_VARIABLES import MIN_STREET_DISTANCE, MAX_MAP_X, MAX_MAP_Y
from model.Car import Car


class Street:

    def __init__(self, max_car_capacity = None):
        self.id = str(uuid.uuid4())
        if max_car_capacity == None:
            self.max_car_capacity = randint(1, 5)
        else:
            self.max_car_capacity = max_car_capacity

        # stores if the street is vertical(v) or horizontal(h)
        self.orientation = random.choice(['h', 'v'])

        if self.orientation == 'h':
            self.current_car_number = {(1, 0): 0, (-1, 0): 0}
        else: # self.orientation == 'v'
            self.current_car_number = {(0, 1): 0, (0, -1): 0}

        # empty list for intersections
        self.intersections = []

        # generate random position for the street
        self.point1 = None
        self.point2 = None
        if self.orientation == 'h':
            # get a random point that can have a street with min distance from the map borders
            self.point1 = (
                random.randint(1, MAX_MAP_X - MIN_STREET_DISTANCE - 1),
                random.randint(1, MAX_MAP_Y)
            )
            # generate a second point at the right of the first one considering the min street distance
            self.point2 = (
                random.randint(self.point1[0] + MIN_STREET_DISTANCE, MAX_MAP_X),
                self.point1[1]
            )
        else:
            # same as above but with vertical streets
            self.point1 = (
                random.randint(1, MAX_MAP_X),
                random.randint(1, MAX_MAP_Y - MIN_STREET_DISTANCE - 1)
            )
            # generate a random point below the first one
            self.point2 = (
                self.point1[0],
                random.randint(self.point1[1] + MIN_STREET_DISTANCE, MAX_MAP_Y)
            )

    def generate_cars(self, simulation):
        """Generate a new car in the current street considering a 1% chance for each empty "space" in the street. 
        The space is the difference between the max car capacity and the current car number.
        The car will be generated in one of the two street end points.
        
        Args:
            simulation (Simulation): the simulation in which the cars are in
        """
        for direction in self.current_car_number:
            if random.randint(0, 100) < 1:
                position = self.point1 if direction > (0, 0) else self.point2

                if self.current_car_number[direction] < self.max_car_capacity:
                    self.current_car_number[direction] += 1
                    simulation.insert_car(Car(position, direction, self))
                    # simulation.cars.append(Car(position = position, direction = direction, current_street = self))

    def update(self, simulation):
        self.generate_cars(simulation)
        self.draw(simulation.screen)
        for intersection in self.intersections:
            intersection.draw(simulation.screen)


    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), self.point1, self.point2)


    def __str__(self) -> str:
        return f'Street: {self.orientation}, {self.point1}, {self.point2}'
                        