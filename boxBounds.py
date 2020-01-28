from math import *

#Box Coordinates
topLeft = (0,0)
topRight = (50,0)
bottomRight = (50,100)
bottomLeft = (0,100)
boxRotation = 10

w = bottomRight[0] - topLeft[0]
h = bottomRight[1] - topLeft[1]


H = w * abs(sin(boxRotation)) + h * abs(cos(boxRotation))
W = w * abs(cos(boxRotation)) + h * abs(sin(boxRotation))
mathAs = abs(sin(boxRotation))
mathCs = abs(cos(boxRotation))

h = (H * mathCs - W * mathCs) / (mathCs**2 - mathAs**2)
w = -(H * mathAs - W * mathCs) / (mathCs**2 - mathAs**2)

XatTopEdge = w * mathCs      #(AE at the picture)
YatRightEdge = h * mathCs    #(DH)
XatBottomEdge = h * mathAs   #(BG)
YatLeftEdge = w * mathAs     #(AF)

print(XatTopEdge)
print(YatRightEdge)
print(XatBottomEdge)
print(YatLeftEdge)
