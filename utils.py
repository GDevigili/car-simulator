import random

from GLOBAL_VARIABLES import MAX_MAP_X, MAX_MAP_Y


def euclidean_distance(p1:tuple, p2:tuple) -> tuple:
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def generate_random_position(map_size:tuple = (MAX_MAP_X, MAX_MAP_Y)) -> tuple:
    return (random.randint(0, map_size[0]/10)*10, random.randint(0, map_size[1]/10)*10)
