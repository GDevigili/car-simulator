import random
import uuid
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
        self.id = str(uuid.uuid4())
        self.set_speed()
        self.position = position
        self.direction = direction
        self.current_street = current_street
        self.stopped = False
        self.distance = 0

    def set_speed(self) -> None:
        self.speed = random.randint(1, 5)

    def change_street(self, intersection):
        
        # randomize the direction
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # remove the opposite of the current direction (the car can't go back)
        directions.remove((self.direction[0] * -1, self.direction[1] * -1))
        new_direction = random.choice(directions)

        # if the car is going to a new street
        if new_direction != self.direction:
            # define the new street
            if self.current_street.orientation == 'h':
                new_street = intersection.vstreet
            else:
                new_street = intersection.hstreet

            if new_street.current_car_number[new_direction] < new_street.max_car_capacity:
                # decrease the number of cars in the old street
                self.current_street.current_car_number[self.direction] -= 1

                # update street and direction
                self.current_street = new_street
                self.direction = new_direction

                # increase the number of cars in the new street
                self.current_street.current_car_number[self.direction] += 1

        self.position = self.move()
        self.set_speed()

    def move(self) -> None:
        # add the direction * speed to the current position
        new_position = (
            self.position[0] + self.direction[0] * self.speed,
            self.position[1] + self.direction[1] * self.speed
        )
        return new_position

    def check_move(self, simulation):
        new_position = self.move()

        # verify if the car is not in a street
        if not is_between(new_position, self.current_street.point1, self.current_street.point2):
            # remove the car from the simulation
            simulation.remove_car(self)
            # decreases the amount of cars in the current street
            self.current_street.current_car_number[self.direction] -= 1
            # delete the object
            del self
            # return False to stop the function
            return 0

        for intersection in self.current_street.intersections:
            # verify if the car is in an intersection
            if intersection.position == self.position:
                # if self.direction in intersection.trafficlight:
                    # change the street (or not)
                    self.change_street(intersection)
                    # move in that direction
                    return 0
                # else:
                    self.stopped = True
                    return 0 
            else:
                # verify if the car will pass by an intersection
                if is_between(intersection.position, self.position, new_position):
                    # go to the intersection
                    self.position = intersection.position
                    # increases the distance
                    self.distance += abs(self.position[0] - intersection.position[0] + self.position[1] - intersection.position[1])
                    return 0
        # updates position                    
        self.position = new_position
        # updates the distance
        self.distance += self.speed

    def export_data(self, simulation):
        return str({
            'type': 'car',
            'id': self.id,
            'speed': self.speed,
            'distance': self.distance,
            'street_id': self.current_street.id,
            'simulation_id': simulation.id,
            'tick_counter': simulation.tick_counter 
        })

    def update(self, simulation):
        self.check_move(simulation)
        self.draw(simulation.screen)
        # if self.stopped:
        #     self.speed = 0
        #simulation.send_message(self.export_data(simulation))

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.position, 5)

            

