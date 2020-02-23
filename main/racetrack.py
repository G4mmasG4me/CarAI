import numpy as np
import pygame
from itertools import cycle

from colors import *

class RaceTrack():
    def __init__(self):
        self.filename = 'tracks/trainingtrack.npz'
        self.tracks = np.load(self.filename, allow_pickle=True)
        self.track1 = self.tracks['track1']
        self.track1 = self.track1.tolist()
        self.track2 = self.tracks['track2']
        self.track2 = self.track2.tolist()
        self.track = self.track1 + self.track2
        self.checkpoints = self.tracks['checkpoints']
        self.checkpoints = self.checkpoints.tolist()
        self.pos = 0

    def update(self, Env):
        for wall in self.track:
            pygame.draw.line(Env.display, black, wall[0], wall[1])
        for wall in self.checkpoints:
            pygame.draw.line(Env.display, green, wall[0], wall[1])
