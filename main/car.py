import pygame
import math

#Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Car():
    def __init__(self, Env):
        self.startX = 75
        self.startY = 400
        self.x = self.startX
        self.y = self.startY
        self.carImg = pygame.image.load('images/bugatti.png')
        self.carImg = pygame.transform.scale(self.carImg, (10, 20))
        self.angle = 0
        self.velocity = 0
        self.brake = 0

        #Driving Values
        self.accelerate = 0.002
        self.decelerate = 0.001
        self.steeringAngle = 0.1
        self.steeringBrake = 0.0001
        self.accelerateBrake = 0.001
        self.decelerateBrake = 0.001
        self.naturalBrake = 0.0005
        self.update(Env)

    def actionMove(self, choice, Env):
        #accelerate
        if choice == 0:
            if self.velocity < 0:
                self.brake += self.accelerateBrake
            else:
                self.velocity += self.accelerate
        #decelerate
        if choice == 1:
            if self.velocity > 0:
                self.brake += self.decelerateBrake
            else:
                self.velocity -= self.decelerate
        #turn left
        if choice == 2:
            if self.velocity != 0:
                self.angle += self.steeringAngle * Env.deltatime
                self.brake += self.steeringBrake
        #turn right
        if choice == 3:
            if self.velocity != 0:
                self.angle -= self.steeringAngle * Env.deltatime
                self.brake += self.steeringBrake

    #Detects if it collides
    def wallCollision(self, RaceTrack):
        totalCrash = False
        for z, corner in enumerate(self.rotatedRectCorners):
            for track in RaceTrack.track:
                def ccw(A,B,C):
                    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

                # Return true if line segments AB and CD intersect
                def intersect(A,B,C,D):
                    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

                next = z + 1
                if next == len(self.rotatedRectCorners):
                    next -= len(self.rotatedRectCorners)
                A = corner
                B = self.rotatedRectCorners[next]
                C = (track[0][0], track[0][1])
                D = (track[1][0], track[1][1])

                crash = intersect(A,B,C,D)
                if crash == True:
                    totalCrash = True
        return totalCrash

    def checkpointCollision(self, RaceTrack):
        totalCrash = False
        for z, corner in enumerate(self.rotatedRectCorners):
            checkpoint = RaceTrack.checkpoints[RaceTrack.pos]
            def ccw(A,B,C):
                return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

                # Return true if line segments AB and CD intersect
            def intersect(A,B,C,D):
                return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

            next = z + 1
            if next > len(self.rotatedRectCorners)-1:
                next -= len(self.rotatedRectCorners)
            A = (corner[0], corner[1])
            B = (self.rotatedRectCorners[next][0], self.rotatedRectCorners[next][1])
            C = (checkpoint[0][0], checkpoint[0][1])
            D = (checkpoint[1][0], checkpoint[1][1])

            crash = intersect(A,B,C,D)

            if crash == True:
                totalCrash = True
                RaceTrack.pos += 1
                if RaceTrack.pos > len(RaceTrack.checkpoints)-1:
                    RaceTrack.pos -= len(RaceTrack.checkpoints)
        return totalCrash


    #Applys the brake to the car
    def speed(self):
        if self.velocity > 0:
            self.velocity -= self.brake
        elif self.velocity < 0:
            self.velocity += self.brake
        self.brake = self.naturalBrake

    #Calculates which way to move and how much
    def move(self, Env):
        self.velocity = 0.0005 * round(self.velocity/0.0005)
        self.velocity = round(self.velocity, 5)
        self.angle = round(self.angle, 2)
        self.x += math.cos(math.radians(-self.angle-90)) * self.velocity * Env.deltatime
        self.y += math.sin(math.radians(-self.angle-90)) * self.velocity * Env.deltatime

    #Gets the rect of the car
    def nonRotatedRect(self):
        self.center = self.carImg.get_rect().center
        self.carRect = self.carImg.get_rect(center = self.center).move(self.x, self.y)
        self.nonRotatedRectCorners = [self.carRect.topleft, self.carRect.topright, self.carRect.bottomright, self.carRect.bottomleft]

    #Gets the rect of the car, which is adjusted so that it is around the body
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

    def drawCar(self, Env):
        Env.display.blit(self.rotatedCar, self.carRect) #Displays it all

    def getState(self):
        return self.angle

    #Calls all the functions as well as blitting it to the screen
    def update(self, Env):
        self.speed() #Gets velocity
        self.move(Env) #Moves it
        self.nonRotatedRect() #Gets the non rotated rect
        self.rotatedRect() #Gets the rotated rect
