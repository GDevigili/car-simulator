import pygame

# Simulation
minutes = 1.0
MAX_EXECUTION_TIME = minutes*60
FPS = 5
FramePerSec = pygame.time.Clock()


# MAP
MAX_MAP_X = 1000
MAX_MAP_Y = 1000

# Street
MIN_STREET_DISTANCE = max(MAX_MAP_X, MAX_MAP_Y)/5