import time
import random
import json
import uuid
from multiprocessing import Process

import pygame
import pika

from model.Intersection import Intersection
from model.Street import Street
from model.Car import Car

from GLOBAL_VARIABLES import *
from utils import get_intersection

def parallel_call_update_cars(simulation, car_list):
    simulation.update_cars(car_list)

class Simulation:
    """Simulates a scenario of the traffic of a city"""

    def __init__(self, n_processes = 10, nbr_streets = 20) -> None:
        # set id
        self.id = str(uuid.uuid4())
        self.n_processes = n_processes

        # randomize the max_duration
        self.duration = random.randint(MIN_EXECUTION_TIME, MAX_EXECUTION_TIME)

        # generate a list of streets
        self.streets = [Street(1) for i in range(nbr_streets)]

        # calculate the intersections
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

        for street in self.streets:
            if street.intersections == []: 
                self.streets.remove(street)
                del street

        self.cars = []

        # define a list of empty lists
        self.car_list = [[] for i in range(self.n_processes)]

    def get_intersection_nbr(self):
        nbr_intersections = 0

        for street in self.streets:
            nbr_intersections += len(street.intersections)
        # each intersection is counted twice
        return nbr_intersections/2

    def update_cars(self, car_list):
        for car in car_list:
            car.update(self)

    def start_connection(self):
       self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
       self.channel = self.connection.channel()

       self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

       self.send_message("Connection successfully established")

    def close_connection(self):
       self.send_message("Closing connection")
       self.connection.close()

    def send_message(self, message):
       self.channel.basic_publish(exchange='logs', routing_key='', body=message)
       print(" [x] Sent %r" % message)

    def export_data(self):
        return str({
            "type": "simulation",
            "id": self.id,
            "nbr_streets": len(self.streets),
            "nbr_intersections": self.get_intersection_nbr(),
            "duration": self.duration,
        })

    def time_message(self):
        return str({
            "type": "time",
            "simulation_id": self.id,
            "time": time.time() - self.start_time,
            "tick_counter": self.tick_counter,
        })

    def insert_car(self, car):
        smallest_list = min(self.car_list, key=len)
        smallest_list.append(car)

    def remove_car(self, car):
        for lst in self.car_list:
            if car in lst:
                lst.remove(car)
                break

    def run(self):
        print(f"running simulation\n  simulation_id {self.id}\n  expected duration: {self.duration} seconds")

        # calculate execution time
        self.start_time = time.time()

        # initialize pygame
        pygame.init()
        running = True

        # fill the screen with white
        self.screen = pygame.display.set_mode((1000, 1000))

        # initialize a connection with the subscriber
        self.start_connection()

        # send a message to the subscriber
        self.send_message(self.export_data())

        # set a tick counter
        self.tick_counter = 0

        # main loop
        while running:

            # reset the screen (fill with white)
            self.screen.fill((255, 255, 255))

            # update the elements
            for street in self.streets:
                street.update(self)
            
            # run parallel processesfor the car updates
            processes = []
            for lst in self.car_list: 
                # p = Process(target=parallel_call_update_cars, args=(self, lst))
                # processes.append(p)
                parallel_call_update_cars(self, lst)

            for p in processes:
                p.start()


            for p in processes:
                p.join()


            # update the display
            pygame.display.update()

            # check if the duration is over
            if time.time() - self.start_time > self.duration:
                running = False

            # check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.tick_counter += 1
            self.send_message(self.time_message())


            # control simulation speed
            pygame.time.Clock().tick(FPS)


        # close the connection
        self.close_connection()
