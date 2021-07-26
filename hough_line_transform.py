import cv2
import numpy as np
import math

img = cv2.imread('sudoku.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect edges
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# detect lines
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

for line in lines:
    rho, theta = line[0]
    a = math.cos(theta)
    b = math.sin(theta)

    x0 = a * rho
    y0 = b * rho

    # x1 stores the rounded off value of (r*cos(theta)-1000*sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r*sin(theta)+1000*cos(theta))
    y1 = int(y0 + 1000 * (a))
    
    # x2 stores the rounded off value of (r*cos(theta)+1000*sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r*sin(theta)-1000*cos(theta))
    y2 = int(y0 - 1000 * (a))

    # draw line on image
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# show image
cv2.imshow('Image', img)

# export processed image
cv2.imwrite('output_houghline.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()