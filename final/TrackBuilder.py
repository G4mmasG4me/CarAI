import pygame
import numpy as np
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

choice1 = int(input('1.Draw Track 2.View Track'))
if choice1 == 1:
    choice2 = int(input("1.Continuous 2.Non-Continuous"))
filename = input('What is the name of the file')

def roundToNearest5(x, y):
    x = 5 * round(x/5)
    y = 5 * round(y/5)
    return x, y

class Text():
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def update(self, mouse):
        self.message = 'Mouse Position - X:' + str(mouse.pos[0]) + ' Y:' + str(mouse.pos[1])
        self.text = self.font.render(self.message, True, black)
        display.blit(self.text, (0,0))

class Mouse():
    def getPos(self):
        self.pos = pygame.mouse.get_pos()
        self.pos = roundToNearest5(self.pos[0], self.pos[1])

class Track():
    def __init__(self):
        self.track1 = []
        self.track2 = []
        self.currentTrack = self.track1
        self.i = 1
        if choice1 == 2:
            self.track = np.load('tracks/' + filename + '.npy', allow_pickle=True)

    def getTrack(self, mouse):
        if self.currentTrack: #if list not empty
            if self.currentTrack[-1][0]:
                if choice2 == 2 and self.i == 2:
                    print(self.currentTrack)
                    print(self.currentTrack[-1])
                    self.currentTrack[-1][1] = mouse.pos
                elif choice2 == 1:
                    self.currentTrack[-1][1] = mouse.pos

    def placeTrack(self, mouse):
        print(self.currentTrack)
        if choice2 == 1:
            self.currentTrack.append([mouse.pos, ()])
        elif choice2 == 2:
            if self.i == 1:
                self.currentTrack.append([mouse.pos])
                self.currentTrack[-1].append([mouse.pos])
                self.i = 2
            elif self.i == 2:
                self.currentTrack[-1].append(mouse.pos)
                self.i = 1

    def drawTrack(self):
        display.fill(white)
        for wall in self.track1:
            pygame.draw.line(display, black, wall[0], wall[1])
        for wall in self.track2:
            pygame.draw.line(display, black, wall[0], wall[1])

    def drawFinishedTrack(self):
        display.fill(white)
        for wall in self.track:
            pygame.draw.line(display, black, wall[0], wall[1])

    def removeLast(self):
        if self.currentTrack:
            self.currentTrack.pop()
            self.i = 1

    def removeAll(self):
        print('Removing All')
        if self.track1:
            self.track1 = []
        if self.track2:
            self.track2 = []
        self.currentTrack = self.track1


    def saveOrSwapTrack(self):
        if self.currentTrack == self.track1:
            if self.track1:
                self.track1.pop()
            self.currentTrack = self.track2
        else:
            if self.track2:
                self.track2.pop()
            track = self.track1 + self.track2
            np.save(filename, track)
            running = False
            quit()
            pygame.quit()

display = pygame.display.set_mode((800, 800))
pygame.display.set_caption('RaceTrack Builder')

clock = pygame.time.Clock()
running = True
mouse = Mouse()
track = Track()
text = Text()
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Left Mouse Button Down")
                if choice1 == 1:
                    track.placeTrack(mouse)
            elif event.button == 3:
                print("Right Mouse Button Down")
                if choice1 == 1:
                    track.removeLast()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                track.saveOrSwapTrack()
            elif event.key == pygame.K_BACKSPACE:
                track.removeAll()
    mouse.getPos()
    if choice1 == 1:
        track.getTrack(mouse)
        track.drawTrack()
        text.update(mouse)
    elif choice1 == 2:
        track.drawFinishedTrack()
        text.update(mouse)
    pygame.display.update()
    clock.tick(60)
