
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
        return x,y
    else:
        return False

def betweenCoords(interceptPoint, line1, line2):
    between = True
    if (min(line1[0][0], line1[1][0]) <= interceptPoint[0] <= max(line1[0][0], line1[1][0])
    and min(line1[0][1], line1[1][1]) <= interceptPoint[1] <= max(line1[0][1], line1[1][1])
    and min(line2[0][0], line2[1][0]) <= interceptPoint[0] <= max(line2[0][0], line2[1][0])
    and min(line2[0][1], line2[1][1]) <= interceptPoint[1] <= max(line2[0][1], line2[1][1])):
        pass
    else:
        between = False

    if between:
        return interceptPoint
    else:
        return False

line1 = ([81.09478438110017,400.0728751440146], [452.0,-71.0])
line2 = ([100,125], [100,675])

line1Equation = line(line1[0], line1[1])
line2Equation = line(line2[0], line2[1])

interceptPoint = intersection(line1Equation, line2Equation)
if interceptPoint:
    interceptPoint = betweenCoords(interceptPoint, line1, line2)

if interceptPoint:
    print("Intersection detected:", interceptPoint)
else:
    print("No single intersection point detected")
