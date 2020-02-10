def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)

    d = (det(*line1), det(*line2))
    try:
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        line2Xmin = min(line2[0][0], line2[1][0])
        line2Xmax = max(line2[0][0], line2[1][0])

        line2Ymin = min(line2[0][1], line2[1][1])
        line2Ymax = max(line2[0][1], line2[1][1])
        print('X:', line2Xmin, '-', line2Xmax)
        print('Y:', line2Ymin, '-', line2Ymax)
        if x >= line2Xmin and x <= line2Ymax and y >= line2Ymin and y <= line2Ymax:
            print('In Range')
        yRan = range(line2Ymin, line2Ymax)
        x = round(x, 0)
        x = int(x)
        print(x in xRan)

        return x, y
    except:
        return 'Does Not Intercept'

print(line_intersection(((80,100), (150,200)), ((200,50), (100,200))))
#line 1 sensor
#line 2 wall
