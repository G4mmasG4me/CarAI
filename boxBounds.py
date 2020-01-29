import math

cX = cY = 50

x = y = 0

theta = -90

tempX = x - cX
tempY = y - cY

rotatedX = ((x - cX) * math.cos(math.radians(theta))) - ((y - cY) * math.sin(math.radians(theta)))
rotatedY = ((x - cX) * math.sin(math.radians(theta))) + ((y - cY) * math.cos(math.radians(theta)))
print(rotatedX + cX)
print(rotatedY + cY)
