line1Start = (10, 20)
line1End = (35, 40)
line2Start = (5, 50)
line2End = (50, 5)

line1Gradient = (line1Start[1] - line1End[1]) / (line1Start[0] - line1End[0])
line1yIntercept = line1Start[1] - (line1Gradient * line1Start[0])
print(line1yIntercept)

line2Gradient = (line2Start[1] - line2End[1]) / (line2Start[0] - line2End[0])
print(line2Gradient)
line2yIntercept = line2Start[1] - (line2Gradient * line2Start[0])
print(line2yIntercept)

line1Equation = ['Y =', line1Gradient, line1yIntercept]
line2Equation = ['Y =', line2Gradient, line2yIntercept]
print(line1Equation)
print(line2Equation)
equation = [line1Gradient, line1yIntercept, '=', line2Gradient, line2yIntercept]

equation = [equation[0] - equation[3], equation[1] - equation[1], '=', equation[3] - equation[3], equation[4] - equation[1]]
equation = [equation[0] / equation[0], '=', equation[4] / equation[0]]
xIntercept = equation[2]
yIntercept = (line1Equation[1] * xIntercept) + line1yIntercept
xIntercept = round(xIntercept, 0)
yIntercept = round(yIntercept, 0)
print(xIntercept)
print(yIntercept)
