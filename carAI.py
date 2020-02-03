import pygame
import math
import numpy as np

pygame.init()
#pygame.mixer.init()

file = 'TokyoDrift.mp3'
#pygame.mixer.music.load(file)
#pygame.mixer.music.play()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

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

class Sensors():
    def __init__(self, Car):#Start(0), End(1), Angle(2), Gradient(3), yIntercept(4), Intercept(5), Intercept Distance(6)
        self.sensors = {'front':[(0,0),(0,0),-90,0,0,(0,0),0],
                        'frontright1':[(0,0),(0,0),-110,0,0,(0,0),0],
                        'frontright2':[(0,0),(0,0),-135,0,0,(0,0),0],
                        'right':[(0,0),(0,0),180,0,0,(0,0),0],
                        'backright1':[(0,0),(0,0),-70,0,0,(0,0),0],
                        'back':[(0,0),(0,0),-45,0,0,(0,0),0],
                        'backleft1':[(0,0),(0,0),0,0,0,(0,0),0],
                        'left':[(0,0),(0,0),90,0,0,(0,0),0],
                        'frontleft2':[(0,0),(0,0),135,0,0,(0,0),0],
                        'frontleft1':[(0,0),(0,0),45,0,0,(0,0),0]}
        self.leftSensors = [self.sensors['front'], self.sensors['frontleft1'], self.sensors['frontleft2'], self.sensors['left'], self.sensors['backleft1'], self.sensors['back']]
        self.rightSensors = [self.sensors['front'], self.sensors['frontright1'], sensors['frontright2'], self.sensors['right'], self.sensors['backright1'], self.sensors['back']]
        self.length = 200
        self.color = blue

    def coordinates(self, Car):
        self.sensors['front'][0] = ((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, (Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2)
        self.sensors['frontright1'][0] = ((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, (Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2)
        self.sensors['frontright2'][0] = (Car.rotatedRectCorners[0][0], Car.rotatedRectCorners[0][1])
        self.sensors['right'][0] = (Car.rotatedRectCorners[0][0], Car.rotatedRectCorners[0][1])
        self.sensors['backright1'][0] = ((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, (Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2)
        self.sensors['back'][0] = (Car.rotatedRectCorners[1][0], Car.rotatedRectCorners[1][1])
        self.sensors['backleft1'][0] = (Car.rotatedRectCorners[1][0], Car.rotatedRectCorners[1][1])
        self.sensors['left'][0] = ((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, (Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2)
        self.sensors['frontleft2'][0] = (Car.rotatedRectCorners[3][0], Car.rotatedRectCorners[3][1])
        self.sensors['frontleft1'][0] = (Car.rotatedRectCorners[2][0], Car.rotatedRectCorners[2][1])

    def gradientyIntercept(self):
        for i in self.sensors:
            self.sensors[i][3] = (self.sensors[i][0][1] - self.sensors[i][1][1]) / (self.sensors[i][0][0] - self.sensors[i][1][0])
            self.sensors[i][4] = self.sensors[i][0][1] - (self.sensors[i][3] * self.sensors[i][0][0])

    def intercept(self):
        for i in RaceTrack.track1:
            for i in self.leftSensors:
        for i in RaceTrack.track2:
            for i in self.rightSensors:

    def createSensors(self, Car, MainRun):
        self.coordinates(Car)
        for i in self.sensors:
            self.sensors[i][1] = ((round((math.cos(math.radians(self.sensors[i][2] + -Car.angle)) * self.length) + self.sensors[i][0][0], 0)), (round((math.sin(math.radians(self.sensors[i][2] + -Car.angle)) * self.length) + self.sensors[i][0][1], 0)))
            pygame.draw.line(MainRun.display, black, self.sensors[i][0], self.sensors[i][1])

class Car():
    def __init__(self):
        self.x = 75
        self.y = 400
        self.carImg = pygame.image.load('bugatti.png')
        self.carImg = pygame.transform.scale(self.carImg, (10, 20))
        self.angle = 0
        self.velocity = 0
        self.brake = 0

    def speed(self):
        if self.velocity > 0:
            self.velocity -= self.brake
        elif self.velocity < 0:
            self.velocity += self.brake
        self.brake = 0.005

    def move(self):
        self.velocity = round(self.velocity, 3)
        self.x += math.cos(math.radians(-self.angle-90)) * self.velocity
        self.y += math.sin(math.radians(-self.angle-90)) * self.velocity

    def nonRotatedRect(self):
        self.center = self.carImg.get_rect().center
        self.carRect = self.carImg.get_rect(center = self.center).move(self.x, self.y)
        self.nonRotatedRectCorners = [self.carRect.topleft, self.carRect.topright, self.carRect.bottomright, self.carRect.bottomleft]

    def rotatedRect(self):
        self.center = self.carImg.get_rect().center
        self.rotatedCar = pygame.transform.rotate(self.carImg, self.angle)
        self.carRect = self.rotatedCar.get_rect(center = self.center).move(self.x, self.y)
        self.center = ((self.nonRotatedRectCorners[0][0] + self.nonRotatedRectCorners[2][0]) / 2, (self.nonRotatedRectCorners[0][1] + self.nonRotatedRectCorners[2][1]) / 2)
        tl = (((self.nonRotatedRectCorners[0][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.nonRotatedRectCorners[0][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.nonRotatedRectCorners[0][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.nonRotatedRectCorners[0][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        tr = (((self.nonRotatedRectCorners[1][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.nonRotatedRectCorners[1][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.nonRotatedRectCorners[1][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.nonRotatedRectCorners[1][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        br = (((self.nonRotatedRectCorners[2][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.nonRotatedRectCorners[2][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.nonRotatedRectCorners[2][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.nonRotatedRectCorners[2][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        bl = (((self.nonRotatedRectCorners[3][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.nonRotatedRectCorners[3][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.nonRotatedRectCorners[3][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.nonRotatedRectCorners[3][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        self.rotatedRectCorners = [tl, tr, br, bl]

    def drawRect(self, main):
        pygame.draw.line(main.display, (255,0,0), self.rotatedRectCorners[0], self.rotatedRectCorners[1])
        pygame.draw.line(main.display, (0,255,0), self.rotatedRectCorners[1], self.rotatedRectCorners[2])
        pygame.draw.line(main.display, (0,0,255), self.rotatedRectCorners[2], self.rotatedRectCorners[3])
        pygame.draw.line(main.display, (0,0,0), self.rotatedRectCorners[3], self.rotatedRectCorners[0])

    def update(self, main):
        self.speed()
        self.move()
        self.nonRotatedRect()
        self.rotatedRect()
        self.drawRect(main)
        main.display.blit(self.rotatedCar, self.carRect)

class Main():
    def __init__(self):
        self.displayWidth = 800
        self.displayHeight = 800
        self.title = 'CarAI'
        self.display = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.main()

    def main(self):
        car = Car()
        sensors = Sensors(car)
        raceTrack = RaceTrack()
        while self.running:
            print('Mouse:', pygame.mouse.get_pos())
            #print(car.velocity)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if car.velocity < 0:
                    car.brake += 0.03
                else:
                    car.velocity += 0.02
            if keys[pygame.K_LEFT]:
                if car.velocity != 0:
                    car.angle += 2.5
                    car.brake += 0.0025
            if keys[pygame.K_RIGHT]:
                if car.velocity != 0:
                    car.angle -= 2.5
                    car.brake += 0.0025
            if keys[pygame.K_DOWN]:
                if car.velocity > 0:
                    car.brake += 0.02
                else:
                    car.velocity -= 0.01

            self.display.fill((255,255,255))
            car.update(self)
            sensors.createSensors(car, self)
            raceTrack.update(self)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
