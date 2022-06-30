import time
import random
import json
import uuid

import pygame
import pika

from model.Intersection import Intersection
from model.Street import Street
from model.Car import Car

from GLOBAL_VARIABLES import *
from utils import get_intersection


class Simulation:
    """Simulates a scenario of the traffic of a city"""

    def __init__(self, nbr_streets = 20) -> None:
        self.streets = [Street(1) for i in range(nbr_streets)]

        self.duration = random.randint(MIN_EXECUTION_TIME, MAX_EXECUTION_TIME)

        # calculate the intersections
        # self.intersections = []
        # iterate over the streets
        for i in range(len(self.streets)):
            # iterate over the streets that weren't already iterated
            for j in range(i + 1, len(self.streets)):
                # verifies if there is a intersection between the two streets
                intersection = get_intersection(self.streets[i], self.streets[j])
                # if there is an intersection
                if intersection:
                    # add the intersection to both streets
                    self.streets[i].intersections.append(intersection)
                    self.streets[j].intersections.append(intersection)

        # remove streets without intersections
        for street in self.streets:
            if street.intersections == []:
                self.streets.remove(street)
                del street

        # define an empty car list
        self.cars = []

    def start_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

    def close_connection(self):
        self.connection.close()

    def send_message(self, message):
        self.channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(" [x] Sent %r" % message)

    def run(self):
        # calculate execution time
        start_time = time.time()

        # initialize pygame
        pygame.init()
        running = True

        # fill the screen with white
        self.screen = pygame.display.set_mode((1000, 1000))

        # main loop
        while running:

            # reset the screen (fill with white)
            self.screen.fill((255, 255, 255))

            # update the elements
            for street in self.streets:
                street.update(self)
                
            for car in self.cars: 
                car.update(self)

            # update the display
            pygame.display.update()

            # check for end conditions
            if time.time() - start_time > self.duration:
                running = False

            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # control simulation speed
            pygame.time.Clock().tick(FPS)

        return time.time() - start_time
