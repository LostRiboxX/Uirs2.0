import cv2
import numpy

img = cv2.imread("frame1gg.png")

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, (5,5))

dilated = cv2.dilate(opening, None, iterations=3)

cv2.imwrite("3.jpg", dilated)