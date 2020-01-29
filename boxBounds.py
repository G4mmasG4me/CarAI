import math

cX = cY = 50

x = y = 0

theta = 90

tempX = x - cX
tempY = y - cY

rotatedX = (tempX * math.cos(math.radians(theta))) - (tempY * math.sin(math.radians(theta)))
rotatedY = (tempX * math.sin(math.radians(theta))) + (tempY * math.cos(math.radians(theta)))
print(rotatedX + cX)
print(rotatedY + cY)

import numpy as np
