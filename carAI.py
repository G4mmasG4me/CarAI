import pygame
import math
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

class Car():
    def __init__(self):
        self.width = 10
        self.height = 25
        self.x = (800 - self.width) / 2
        self.y = (800 - self.height) / 2
        self.xSpeed = 0
        self.ySpeed = 0
        self.angle = 0
        self.img = pygame.image.load('bugatti.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))

    def update(self, MainRun):
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.rect = self.img.get_rect(topleft=(self.x, self.y))
        MainRun.display.blit(self.img, (self.x, self.y))

class Sensors():
    def __init__(self, Car):
        self.sensors = {'front':[Car.rect.midtop,-90],
                        'frontleft1':[Car.rect.midtop,-110],
                        'frontleft2':[Car.rect.topleft,-135],
                        'left':[Car.rect.topleft,180],
                        'frontright1':[Car.rect.midtop,-70],
                        'frontright2':[Car.rect.topright,-45],
                        'right':[Car.rect.topright,0],
                        'back':[Car.rect.midbottom,90],
                        'backleft1':[Car.rect.bottomleft,135],
                        'backright1':[Car.rect.bottomright, 45]}
        self.length = 500
        self.color = blue

    def createSensors(self, Car, MainRun):
        for i in self.sensors:
            self.x = round((math.cos(math.radians(self.sensors[i][1] + Car.angle)) * self.length) + self.sensors[i][0][0], 0)
            self.y = round((math.sin(math.radians(self.sensors[i][1] + Car.angle)) * self.length) + self.sensors[i][0][1], 0)
            #print(self.sensors[i][0])
            pygame.draw.line(MainRun.display, black, self.sensors[i][0], (self.x, self.y))

    #def update(self, MainRun, Car):

class RaceTrack():
    def  __init__(self):
        self.track = [[(50, 700), (50, 100)],
                      [(50, 100), (100, 50)],
                      [(100, 50), (200, 50)],
                      [(200, 50), (250, 100)],
                      [(250, 100), (250, 200)]]


    def createTrack(self, MainRun):
        for i in self.track:
            print(i[0])
            pygame.draw.line(MainRun.display, black, i[0], i[1])
            print('Track Made')


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
        raceTrack.createTrack(self)
        while running == True:
            print('Mouse', pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()


            car.update(self)
            sensors.createSensors(car, self)
            pygame.display.update()
            clock.tick(1)

if __name__ == '__main__':
    MainRun()
