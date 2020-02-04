def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    d = (det(*line1), det(*line2))
    print(line1)
    print(*line1)
    try:
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y
    except:
        return 'Does Not Intercept'

print(line_intersection(((80,100), (80,200)), ((200,50), (200,150))))
