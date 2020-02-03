sensors = {'front':[(0,0),(0,0),-90],
           'frontright1':[(0,0),(0,0),-110],
           'frontright2':[(0,0),(0,0),-135],
           'right':[(0,0),(0,0),180],
           'backright1':[(0,0),(0,0),-70],
           'back':[(0,0),(0,0),-45],
           'backleft1':[(0,0),(0,0),0],
           'left':[(0,0),(0,0),90],
           'frontleft2':[(0,0),(0,0),135],
           'frontleft1':[(0,0),(0,0),45]}
leftSensors = [sensors['front'], sensors['frontleft1'], sensors['frontleft2'], sensors['left'], sensors['backleft1'], sensors['back']]
leftSensors = [sensors['front'], sensors['frontright1'], sensors['frontright2'], sensors['right'], sensors['backright1'], sensors['back']]

for i in leftSensors:
    print(i)
