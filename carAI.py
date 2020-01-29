import pygame
import math
import numpy as np

pygame.init()
pygame.mixer.init()

file = 'TokyoDrift.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Interception():
    def update(sensors):
        self.leftSensors = sensors.sensors
        self.rightSensors = sensors.sensors

class RaceTrack():
    def __init__(self):
        self.filename = 'trainingtrack.npz'
        self.tracks = np.load(self.filename, allow_pickle=True)
        self.track1 = self.tracks['track1']
        self.track2 = self.tracks['track2']
    def update(self, MainRun):
        for wall in self.track1:
            pygame.draw.line(MainRun.display, black, wall[0], wall[1])
        for wall in self.track2:
            pygame.draw.line(MainRun.display, black, wall[0], wall[1])

class Car():
    def __init__(self):
        self.width = 10
        self.height = 25
        self.x = 400
        self.y = 400
        self.speed = 0
        self.angle = 0
        self.img = pygame.image.load('bugatti.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.img.get_rect(center=(self.x, self.y))

    #def speed(self):


    #def brake(self)




    def update(self, MainRun):
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img, -self.angle)
        self.rect = self.img.get_rect(center=(self.x, self.y))
        MainRun.display.blit(self.img, (self.x - (self.width / 2), self.y - (self.height / 2)))

class Sensors():
    def __init__(self, Car):
        self.sensors = {'front':[Car.rect.midtop,(0,0),-90],
                        'frontright1':[Car.rect.midtop,(0,0),-110],
                        'frontright2':[Car.rect.topleft,(0,0),-135],
                        'right':[Car.rect.topleft,(0,0),180],
                        'backright1':[Car.rect.midtop,(0,0),-70],
                        'back':[Car.rect.topright,(0,0),-45],
                        'backleft1':[Car.rect.topright,(0,0),0],
                        'left':[Car.rect.midbottom,(0,0),90],
                        'frontleft2':[Car.rect.bottomleft,(0,0),135],
                        'frontleft1':[Car.rect.bottomright,(0,0),45]}

    def coordinates(self):
        cX = (Car.rect.topleft[0] + Car.rect.bottomright[0]) / 2
        cY = (Car.rect.topleft[1] + Car.rect.bottomright[1]) / 2
        tl = (((Car.rect.topleft[0] - cX) * math.cos(math.radians(Car.angle))) - ((Car.rect.topleft[1] - cY) * math.sin(math.radians(Car.angle))), ((Car.rect.topleft[0] - cX) * math.sin(math.radians(Car.angle))) + ((Car.rect.topleft[1] - cY) * math.cos(math.radians(Car.angle))))
        tr = (((Car.rect.topright[0] - cX) * math.cos(math.radians(Car.angle))) - ((Car.rect.topright[1] - cY) * math.sin(math.radians(Car.angle))), ((Car.rect.topright[0] - cX) * math.sin(math.radians(Car.angle))) + ((Car.rect.topright[1] - cY) * math.cos(math.radians(Car.angle))))
        br = (((Car.rect.bottomright[0] - cX) * math.cos(math.radians(Car.angle))) - ((Car.rect.bottomright[1] - cY) * math.sin(math.radians(Car.angle))), ((Car.rect.bottomright[0] - cX) * math.sin(math.radians(Car.angle))) + ((Car.rect.bottomright[1] - cY) * math.cos(math.radians(Car.angle))))
        bl = (((Car.rect.bottomleft[0] - cX) * math.cos(math.radians(Car.angle))) - ((Car.rect.bottomleft[1] - cY) * math.sin(math.radians(Car.angle))), ((Car.rect.bottomleft[0] - cX) * math.sin(math.radians(Car.angle))) + ((Car.rect.bottomleft[1] - cY) * math.cos(math.radians(Car.angle))))
        self.sensors[0][0] = ((tl[0] + tr[0]) / 2, (tl[1] + tr[1] / 2))
        self.sensors[1][0] = ((tl[0] + tr[0]) / 2, (tl[1] + tr[1] / 2))
        self.sensors[2][0] = tl
        self.sensors[3][0] = tl
        self.sensors[4][0] = ((tl[0] + tr[0]) / 2, (tl[1] + tr[1]) / 2)
        self.sensors[5][0] = tr
        self.sensors[6][0] = tr
        self.sensors[7][0] = ((bl[0] + br[0]) / 2, (bl[1] + br[1]) / 2)
        self.sensors[8][0] = bl
        self.sensors[9][0] = br
        #for i in self.sensors:
            #self.startX =
            #self.startY =
        self.length = 200
        self.color = blue

    def createSensors(self, Car, MainRun):
        for i in self.sensors:
            #self.startX =
            #self.startY =
            self.endX = round((math.cos(math.radians(self.sensors[i][2] + Car.angle)) * self.length) + self.sensors[i][0][0], 0)
            self.endY = round((math.sin(math.radians(self.sensors[i][2] + Car.angle)) * self.length) + self.sensors[i][0][1], 0)
            pygame.draw.line(MainRun.display, black, self.sensors[i][0], (self.endX, self.endY))

    #def update(self, MainRun, Car):


class MainRun():
    def __init__(self):
        self.width = 800
        self.height = 800
        self.title = 'CarAI'
        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.main()

    def main(self):

        clock = pygame.time.Clock()
        running = True
        car = Car()
        sensors = Sensors(car)
        raceTrack = RaceTrack()
        self.display.fill(white)
        while running == True:
            print('Mouse', pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            raceTrack.update(self)
            car.update(self)
            sensors.createSensors(car, self)
            pygame.display.update()
            clock.tick(1)

if __name__ == '__main__':
    MainRun()
