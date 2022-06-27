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

    def get_intersections(self, simulation):
        for street in simulation.streets:
            if self.orientation == street.orientation:
                pass
            else:
                if self.orientation == 'h':
                    # verifies if st.x is between self.x1 and self.x2 
                    # and if self.y is between st.y1 and st.y2
                    if street.point1[0] >= self.point1[0] \
                    and street.point2[0] <= self.point2[0] \
                    and self.point1[1] >= street.point2[1] \
                    and self.point2[1] <= street.point2[1]:
                        # the intersection's x is the vertical street x
                        int_x = street.point1[0]
                        # the intersection's y is the horizontal street y
                        int_y = self.point1[1]
                        intersection = Intersection((int_x, int_y), self, street)
                        self.intersections.append(intersection)
                        street.intersections.append(intersection)
                

        # for street in simulation.streets:
        #     # pass if the streets are parallel
        #     if self.orientation == street.orientation:
        #         pass
        #     if self.orientation == 'h':
        #         if  self.points[0][0] <= street.points[0][0] and \
        #             self.points[1][0] >= street.points[0][0] and \
        #             self.points[0][1] <= street.points[0][1] and \
        #             self.points[1][1] >= street.points[0][1]:

        #             intersection = Intersection(
        #                 position = (self.points[0][1], street.points[0][0]),
        #                 hstreet = self, vstreet = street, 
        #             )
        #             self.intersections.append(intersection)
        #             street.intersections.append(intersection)
        #             simulation.intersections.append(intersection)

            # if self.orientation == 'h':
            #     if street.orientation == 'v':
            #         if self.points[0][0] <= street.points[0][0] and self.points[1][0] >= street.points[0][0]:
                        
                        