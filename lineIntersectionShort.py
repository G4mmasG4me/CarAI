line1Start = (10, 20)
line1End = (35, 40)
line2Start = (5, 50)
line2End = (50, 5)

for i in range(60000):
    line1Gradient = (line1Start[1] - line1End[1]) / (line1Start[0] - line1End[0])
    line1yIntercept = line1Start[1] - (line1Gradient * line1Start[0])

    line2Gradient = (line2Start[1] - line2End[1]) / (line2Start[0] - line2End[0])
    line2yIntercept = line2Start[1] - (line2Gradient * line2Start[0])

    xIntercept = (line2yIntercept - line1yIntercept) / (line1Gradient - line2Gradient)
    yIntercept = (line1Gradient * xIntercept) + line1yIntercept
    xIntercept = round(xIntercept, 0)
    yIntercept = round(yIntercept, 0)
