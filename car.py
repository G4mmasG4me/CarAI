import pygame
import time
import math

running = True

class Car():
    def __init__(self):
        self.x = 100
        self.y = 100
        self.carImg = pygame.image.load('bugatti.png')
        self.carImg = pygame.transform.scale(self.carImg, (400, 800))
        self.angle = 45
        self.velocity = 0

    def move(self):
        self.velocity = round(self.velocity, 2)
        self.x += math.cos(math.radians(-self.angle-90)) * self.velocity
        self.y += math.sin(math.radians(-self.angle-90)) * self.velocity
        print(self.velocity)

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
        self.move()
        self.nonRotatedRect()
        self.rotatedRect()
        self.drawRect(main)
        main.display.blit(self.rotatedCar, self.carRect)


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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                car.velocity += 0.1
            if keys[pygame.K_LEFT]:
                car.angle += 1
            if keys[pygame.K_RIGHT]:
                car.angle -= 1
            if keys[pygame.K_DOWN]:
                car.velocity -= 0.05

            self.display.fill((255,255,255))
            car.update(self)
            pygame.display.update()
            self.clock.tick(30)

if __name__ == '__main__':
    main = Main()
