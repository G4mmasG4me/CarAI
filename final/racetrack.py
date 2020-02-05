import numpy as np
import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class RaceTrack():
    def __init__(self):
        self.filename = 'tracks/trainingtrack.npy'
        self.track = np.load(self.filename, allow_pickle=True)

    def update(self, MainRun):
        for wall in self.track:
            pygame.draw.line(MainRun.display, black, wall[0], wall[1])
