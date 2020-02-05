import pygame
import math
import numpy as np
from car import Car
from racetrack import RaceTrack
from sensors import Sensors

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

class Main():
    def __init__(self):
        self.displayWidth = 800
        self.displayHeight = 800
        self.title = 'CarAI'
        self.display = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.deltatime = self.clock.tick(60)
        self.running = True
        self.main()

    def main(self):
        car = Car()
        sensors = Sensors(car)
        raceTrack = RaceTrack()
        while self.running:
            #print(self.clock.get_fps())
            #print('Mouse:', pygame.mouse.get_pos())
            print(car.velocity)
            #print(self.deltatime)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                if car.velocity < 0:
                    car.brake += car.accelerateBrake
                else:
                    car.velocity += car.accelerate
            if keys[pygame.K_LEFT]:
                if car.velocity != 0:
                    car.angle += car.steeringAngle * self.deltatime
                    car.brake += car.steeringBrake
            if keys[pygame.K_RIGHT]:
                if car.velocity != 0:
                    car.angle -= car.steeringAngle * self.deltatime
                    car.brake += car.steeringBrake
            if keys[pygame.K_DOWN]:
                if car.velocity > 0:
                    car.brake += car.decelerateBrake
                else:
                    car.velocity -= car.decelerate

            self.display.fill(white)
            car.update(self)
            sensors.update(car, raceTrack, self)
            raceTrack.update(self)
            pygame.display.update()
            self.deltatime = self.clock.tick(60)

if __name__ == '__main__':
    Main = Main()
