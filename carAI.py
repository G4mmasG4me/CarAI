import pygame
import math
pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Car():
    def __init__(self):
        self.width = 25
        self.height = 50
        self.x = (800 - self.width) / 2
        self.y = (800 - self.height) / 2
        self.xSpeed = 0
        self.ySpeed = 0
        self.angle = 0
        self.img = pygame.image.load('bugatti.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.center = self.img.get_rect().center
        self.rect = self.img.get_rect(center = self.center).move(self.x, self.y)

    def update(self, MainRun):
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.img = pygame.transform.rotate(self.img, self.angle)
        self.center = self.img.get_rect().center
        self.rect = self.img.get_rect(center = self.center).move(self.x, self.y)
        MainRun.display.blit(self.img, (self.x, self.y))

class Sensors():
    def __init__(self, Car):
        self.sensors = {'front':[Car.rect.midtop,-90,(50,0,0)],
                        'frontleft1':[Car.rect.midtop,-110,(100,0,0)],
                        'frontleft2':[Car.rect.topleft,-135,(150,0,0)],
                        'left':[Car.rect.topleft,-180,(200,0,0)],
                        'frontright1':[Car.rect.midtop,-70,(250,0,0)],
                        'frontright2':[Car.rect.topright,-45,(0,50,0)],
                        'right':[Car.rect.topright,0,(0,100,0)],
                        'back':[Car.rect.midbottom,90,(0,150,0)],
                        'backleft1':[Car.rect.bottomleft,135,(0,200,0)],
                        'backright1':[Car.rect.bottomright, 45,(0,250,0)]}
        self.length = 50
        self.color = blue

    def createSensors(self, Car, MainRun):
        for i in self.sensors:
            self.x = (math.cos(math.radians(self.sensors[i][1] + Car.angle)) * self.length) + Car.x
            self.y = (math.sin(math.radians(self.sensors[i][1] + Car.angle)) * self.length) + Car.y
            print('Coordinates', self.x, self.y)
            print('Angle', self.sensors[i][1])
            pygame.draw.line(MainRun.display, self.sensors[i][2], self.sensors[i][0], (self.x, self.y))

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
        while running == True:
            #print('Mouse', pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            self.display.fill(white)
            car.update(self)
            sensors.createSensors(car, self)
            pygame.display.update()
            clock.tick(1)

if __name__ == '__main__':
    MainRun()
