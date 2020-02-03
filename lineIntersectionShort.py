line1Start = (10, 20)
line1End = (20, 30)
line2Start = (10, 10)
line2End = (20, 20)

for i in range(60000):
    line1Gradient = (line1Start[1] - line1End[1]) / (line1Start[0] - line1End[0])
    line1yIntercept = line1Start[1] - (line1Gradient * line1Start[0])

    line2Gradient = (line2Start[1] - line2End[1]) / (line2Start[0] - line2End[0])
    line2yIntercept = line2Start[1] - (line2Gradient * line2Start[0])

    print(line2yIntercept - line1yIntercept)
    xIntercept = (line2yIntercept - line1yIntercept) / (line1Gradient - line2Gradient)
    yIntercept = (line1Gradient * xIntercept) + line1yIntercept
    xIntercept = round(xIntercept, 0)
    yIntercept = round(yIntercept, 0)
    intercept = (xIntercept, yIntercept)
    print(intercept)
    print(i)
