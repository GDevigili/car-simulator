import random

from model.Intersection import Intersection
from GLOBAL_VARIABLES import MAX_MAP_X, MAX_MAP_Y


def euclidean_distance(p1:tuple, p2:tuple) -> tuple:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def generate_random_position(map_size:tuple = (MAX_MAP_X, MAX_MAP_Y)) -> tuple:
    return (random.randint(0, map_size[0]/10)*10, random.randint(0, map_size[1]/10)*10)

def get_intersection(st1, st2):
    hstreet = None
    vstreet = None

    # check if the streets are not the same
    if st1 == st2:
        return None
    # check if the streets are paralel
    elif st1.orientation == st2.orientation:
        return None
    # define which of the streets is the vertical one and which is the horizontal one
    elif st1.orientation == 'h':
        hstreet = st1
        vstreet = st2
    elif st2.orientation == 'h':
        hstreet = st2
        vstreet = st1
    else:
        raise ValueError('Invalid street orientation')

    # if the vertical street points are between the horizontal street x's
    if vstreet.point1[0] >= hstreet.point1[0] and vstreet.point2[0] <= hstreet.point2[0]:
        # if the horizontal street points are between the vertical street y's
        if hstreet.point1[1] >= vstreet.point1[1] and hstreet.point1[1] <= vstreet.point2[1]:
            # the intersection has the x of vstreet and y of hstreet (they are constants as the streets are perpendicular to the map)
            return Intersection(position = (vstreet.point1[0], hstreet.point1[1]), vstreet = vstreet, hstreet = hstreet)

    # if one of the condition above are false, the streets are not intersecting
    return None

def is_between(p, a, b) -> bool:
    if (p[0] >= a[0] and p[0] <= b[0]) or (p[0] >= b[0] and p[0] <= a[0]):
        if (p[1] >= a[1] and p[1] <= b[1]) or (p[1] >= b[1] and p[1] <= a[1]):
            return True
    return False

def get_car_list(cars, streets):
    car_list = {}
    # create empty lists for every street
    for street in streets:
        car_list[street] = []
    # add the cars to the list
    for car in cars:
        car_list[car.current_street].append(car)