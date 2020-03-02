import pygame
import math

#Colours
from colors import *

class Sensors():
    def __init__(self, Car, Ractrack):#Start(0), End(1), Angle(2), Intercept(3), Intercept Distance(4)
        self.sensors = {'front':[(0,0),(0,0),-90,(-0,-0),-0],
                        'frontright1':[(0,0),(0,0),-70,(0,0),0],
                        'frontright2':[(0,0),(0,0),-45,(0,0),0],
                        'right':[(0,0),(0,0),0,(0,0),0],
                        'backright1':[(0,0),(0,0),70,(0,0),0],
                        'back':[(0,0),(0,0),90,(0,0),0],
                        'backleft1':[(0,0),(0,0),110,(0,0),0],
                        'left':[(0,0),(0,0),180,(0,0),0],
                        'frontleft2':[(0,0),(0,0),-135,(0,0),0],
                        'frontleft1':[(0,0),(0,0),-110,(0,0),0]}
        self.length = 600
        self.color = blue
        self.state = [0,0,0,0,0,0,0,0,0,0]

    #Sets the position of the start of the sensor
    def startCoord(self, Car):
        self.sensors['front'][0] = (round((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, 0), round((Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2, 0))
        self.sensors['frontright1'][0] = (round((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, 0), round((Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2, 0))
        self.sensors['frontright2'][0] = (round(Car.rotatedRectCorners[1][0], 0), round(Car.rotatedRectCorners[1][1], 0))
        self.sensors['right'][0] = (round((Car.rotatedRectCorners[1][0] + Car.rotatedRectCorners[2][0]) / 2, 0), round((Car.rotatedRectCorners[1][1] + Car.rotatedRectCorners[2][1]) / 2, 0))
        self.sensors['backright1'][0] = (round((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, 0), round((Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2, 0))
        self.sensors['back'][0] = (round((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, 0), round((Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2, 0))
        self.sensors['backleft1'][0] = (round((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, 0), round((Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2, 0))
        self.sensors['left'][0] = (round((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[0][0]) / 2, 0), round((Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[0][1]) / 2, 0))
        self.sensors['frontleft2'][0] = (round(Car.rotatedRectCorners[0][0], 0), round(Car.rotatedRectCorners[0][1], 0))
        self.sensors['frontleft1'][0] = (round((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, 0), round((Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2, 0))

    #Sets the position of the end of the sensor
    def sensorValues(self, Car):
        for sensor in self.sensors:
            x = round((math.cos(math.radians(self.sensors[sensor][2] + -Car.angle)) * self.length) + self.sensors[sensor][0][0], 0)
            y = round((math.sin(math.radians(self.sensors[sensor][2] + -Car.angle)) * self.length) + self.sensors[sensor][0][1], 0)
            self.sensors[sensor][1] = (x, y)

    #Calculates the intercept between the track and the sensor
    def intercept(self, RaceTrack):
        #Calculating function
        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0]*p2[1] - p2[0]*p1[1])
            return A, B, -C

        def intersection(L1, L2):
            D  = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return (x,y)
            else:
                return False

        def betweenCoords(interceptPoint, line1, line2):

            if (min(line1[0][0], line1[1][0]) <= round(interceptPoint[0], 0) <= max(line1[0][0], line1[1][0], 0)
            and min(line1[0][1], line1[1][1]) <= round(interceptPoint[1], 0) <= max(line1[0][1], line1[1][1], 0)
            and min(line2[0][0], line2[1][0]) <= round(interceptPoint[0], 0) <= max(line2[0][0], line2[1][0], 0)
            and min(line2[0][1], line2[1][1]) <= round(interceptPoint[1], 0) <= max(line2[0][1], line2[1][1], 0)):
                return interceptPoint
            else:
                return False

        for sensor in self.sensors:
            self.sensors[sensor][3] = (1000,1000)
            self.sensors[sensor][4] = 10000

        for trackLine in RaceTrack.track:
            for sensor in self.sensors:

                trackLineEquation = line(trackLine[0], trackLine[1])
                sensorLineEquation = line(self.sensors[sensor][0], self.sensors[sensor][1])

                interceptPoint = intersection(trackLineEquation, sensorLineEquation)
                if interceptPoint:
                    interceptPoint = betweenCoords(interceptPoint, trackLine, (self.sensors[sensor][0], self.sensors[sensor][1]))

                if interceptPoint:
                    interceptDistance = math.sqrt((self.sensors[sensor][0][0] - interceptPoint[0])**2 + (self.sensors[sensor][0][1] - interceptPoint[1])**2)

                    if interceptDistance < self.sensors[sensor][4]:
                        self.sensors[sensor][3] = (int(interceptPoint[0]), int(interceptPoint[1]))
                        self.sensors[sensor][4] = int(interceptDistance)
                        self.sensors[sensor][1] = interceptPoint


    def sensorStates(self):
        for sensor in self.sensors:
            self.state[list(self.sensors.keys()).index(sensor)] = self.sensors[sensor][4]


    #Draws the sensors
    def drawSensors(self, Env):
        for sensor in self.sensors:
            pygame.draw.line(Env.display, black, self.sensors[sensor][0], self.sensors[sensor][1])
            pygame.draw.circle(Env.display, red, self.sensors[sensor][3], 4)

    def getState(self):
        return self.state

    #Calls all the functions
    def update(self, Car, RaceTrack):
        self.startCoord(Car)
        self.sensorValues(Car)
        self.intercept(RaceTrack)
        self.sensorStates()
