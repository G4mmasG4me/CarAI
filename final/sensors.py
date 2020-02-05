import pygame
import math

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Sensors():
    def __init__(self, Car):#Start(0), End(1), Angle(2), Intercept(3), Intercept Distance(4)
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


    def startCoord(self, Car):
        self.sensors['front'][0] = ((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, (Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2)
        self.sensors['frontright1'][0] = ((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, (Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2)
        self.sensors['frontright2'][0] = Car.rotatedRectCorners[1]
        self.sensors['right'][0] = ((Car.rotatedRectCorners[1][0] + Car.rotatedRectCorners[2][0]) / 2, (Car.rotatedRectCorners[1][1] + Car.rotatedRectCorners[2][1]) / 2)
        self.sensors['backright1'][0] = ((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, (Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2)
        self.sensors['back'][0] = ((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, (Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2)
        self.sensors['backleft1'][0] = ((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[2][0]) / 2, (Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[2][1]) / 2)
        self.sensors['left'][0] = ((Car.rotatedRectCorners[3][0] + Car.rotatedRectCorners[0][0]) / 2, (Car.rotatedRectCorners[3][1] + Car.rotatedRectCorners[0][1]) / 2)
        self.sensors['frontleft2'][0] = Car.rotatedRectCorners[0]
        self.sensors['frontleft1'][0] = ((Car.rotatedRectCorners[0][0] + Car.rotatedRectCorners[1][0]) / 2, (Car.rotatedRectCorners[0][1] + Car.rotatedRectCorners[1][1]) / 2)

    def sensorValues(self, Car):
        for i in self.sensors:
            self.sensors[i][1] = ((round((math.cos(math.radians(self.sensors[i][2] + -Car.angle)) * self.length) + self.sensors[i][0][0], 0)), (round((math.sin(math.radians(self.sensors[i][2] + -Car.angle)) * self.length) + self.sensors[i][0][1], 0)))

    def intercept(self, RaceTrack, Main):
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        for sensor in self.sensors:
            for trackLine in RaceTrack.track:
                xdiff = (trackLine[0][0] - trackLine[1][0], self.sensors[sensor][0][0] - self.sensors[sensor][1][0])
                ydiff = (trackLine[0][1] - trackLine[1][1], self.sensors[sensor][0][1] - self.sensors[sensor][1][1])

                div = det(xdiff, ydiff)

                d = (det(trackLine[0], trackLine[1]), det(self.sensors[sensor][0], self.sensors[sensor][1]))

                x = det(d, xdiff) / div
                y = det(d, ydiff) / div
                if math.isnan(x) or math.isinf(x) or math.isnan(y) or math.isinf(y):
                    x = 0
                    y = 0
                x = int(round(x, 0))
                y = int(round(y, 0))

                line1Xmin = min(int(trackLine[0][0]), int(trackLine[1][0]))
                line1Xmax = max(int(trackLine[0][0]), int(trackLine[1][0]))
                line1Ymin = min(int(trackLine[0][1]), int(trackLine[1][1]))
                line1Ymax = max(int(trackLine[0][1]), int(trackLine[1][1]))
                line2Xmin = min(int(self.sensors[sensor][0][0]), int(self.sensors[sensor][1][0]))
                line2Xmax = max(int(self.sensors[sensor][0][0]), int(self.sensors[sensor][1][0]))
                line2Ymin = min(int(self.sensors[sensor][0][1]), int(self.sensors[sensor][1][1]))
                line2Ymax = max(int(self.sensors[sensor][0][1]), int(self.sensors[sensor][1][1]))

                if not x >= line1Xmin or not x <= line1Xmax or not y >= line1Ymin or not y <= line1Ymax:
                    x = 0
                    y = 0
                if not x >= line2Xmin or not x <= line2Xmax or not y >= line2Ymin or not y <= line2Ymax:
                    x = 0
                    y = 0

                intercept = (x, y)
                pygame.draw.circle(Main.display, red, intercept, 4)
                interceptDistance = math.sqrt((self.sensors[sensor][0][0] - intercept[0])**2 + (self.sensors[sensor][0][1] - intercept[1])**2)

    def drawIntercept(self, Main):
        for sensor in self.sensors:
            pygame.draw.circle(Main.display, red, self.sensors[sensor][3], 4)

    def createSensors(self, Main):
        for sensor in self.sensors:
            pygame.draw.line(Main.display, black, self.sensors[sensor][0], self.sensors[sensor][1])

    def update(self, Car, RaceTrack, Main):
        self.startCoord(Car)
        self.sensorValues(Car)
        self.intercept(RaceTrack, Main)
        #self.drawIntercept(Main)
        self.createSensors(Main)
