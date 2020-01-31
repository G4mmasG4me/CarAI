import pygame
import time
import math

running = True

class Car():
    def __init__(self):
        self.carImg = pygame.image.load('bugatti.png')
        self.carImg = pygame.transform.scale(self.carImg, (50, 100))
        self.angle = 0
        self.center = self.carImg.get_rect().center
        self.car = pygame.transform.rotate(self.carImg, self.angle)
        self.carRect = self.car.get_rect(center = self.center).move(400, 400)
        self.originalCoords = [self.carRect.topleft, self.carRect.topright, self.carRect.bottomright, self.carRect.bottomleft]

    def boxRect(self):
        self.angle += 90
        self.center = self.carImg.get_rect().center
        self.car = pygame.transform.rotate(self.carImg, self.angle)
        self.carRect = self.car.get_rect(center = self.center).move(400, 400)
        print(self.originalCoords[0][0])
        self.center = ((self.originalCoords[0][0] + self.originalCoords[2][0]) / 2, (self.originalCoords[0][1] + self.originalCoords[2][1]) / 2)
        tl = (((self.originalCoords[0][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.originalCoords[0][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.originalCoords[0][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.originalCoords[0][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        tr = (((self.originalCoords[1][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.originalCoords[1][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.originalCoords[1][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.originalCoords[1][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        br = (((self.originalCoords[2][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.originalCoords[2][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.originalCoords[2][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.originalCoords[2][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        bl = (((self.originalCoords[3][0] - self.center[0]) * math.cos(math.radians(-self.angle))) - ((self.originalCoords[3][1] - self.center[1]) * math.sin(math.radians(-self.angle))) + self.center[0], ((self.originalCoords[3][0] - self.center[0]) * math.sin(math.radians(-self.angle))) + ((self.originalCoords[3][1] - self.center[1]) * math.cos(math.radians(-self.angle))) + self.center[1])
        self.corners = [tl, tr, br, bl]

    def drawRect(self, main):
        pygame.draw.line(main.display, (255,0,0), self.corners[0], self.corners[1])
        pygame.draw.line(main.display, (0,255,0), self.corners[1], self.corners[2])
        pygame.draw.line(main.display, (0,0,255), self.corners[2], self.corners[3])
        pygame.draw.line(main.display, (0,0,0), self.corners[3], self.corners[0])

    def update(self, main):
        self.boxRect()
        self.drawRect(main)
        main.display.blit(self.car, self.carRect)


class Main():
    def __init__(self):
        self.displayWidth = 800
        self.displayHeight = 800
        self.display = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        self.clock = pygame.time.Clock()
        self.running = True
        self.main()


    def main(self):
        car = Car()
        while self.running:
            print('Mouse:', pygame.mouse.get_pos())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            self.display.fill((255,255,255))
            car.update(self)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
