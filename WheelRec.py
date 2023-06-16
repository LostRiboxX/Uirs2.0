import cv2
import numpy as np

def get_wheel_frag(conts, wheel_coords):
    points = []
    for point in wheel_coords:
        tmp = []
        for i, contour in enumerate(conts):
            result = cv2.pointPolygonTest(contour, point, True)
            tmp.append(result)
        points.append(tmp.index(max(tmp)))
    return points