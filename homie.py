import cv2
import numpy as np
import math


def drawwheels(imgnamecont: str, imagename: str, point: int, angle0) -> None:
    angle = angle0 + 180
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 500)
    fontScale = 2
    fontColor = (255, 255, 255)
    thickness = 2
    lineType = 2

    img = cv2.imread(imgnamecont)
    image = cv2.imread(imagename)

    median_blur = cv2.medianBlur(img, 15)
    gray = cv2.cvtColor(median_blur, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    j = 0
    contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    massbrown = []
    contsmass = []
    for i in contours:
        area = cv2.contourArea(i)
        if 4700 < area < 100000:
            M = cv2.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                if j == point:
                    pointpos = (cx + 5, cy - 5)
                cv2.drawContours(image, [i[0] - 200, i[1] - 200], -1, (0, 255, 0), 2)
                cv2.circle(image, (cx + 5, cy - 5), 10, (0, 0, 255), -1)
                cv2.putText(image, str(j), (cx - 10, cy - 10), font, fontScale, fontColor, thickness, lineType)
                massx = ["cx brown", cx, "cy brown: ", cy]
                mass1 = [cx - 5, cy - 5]
                massbrown.append(mass1)
                contsmass.append(i)
                j += 1

    center_x, center_y = pointpos[0], pointpos[1]

    radius1 = 90

    angle1 = angle * math.pi / 180
    angle2 = (2 * math.pi / 3) + (angle * math.pi / 180)
    angle3 = (4 * math.pi / 3) + (angle * math.pi / 180)

    center1_x = int(center_x + radius1 * math.cos(angle1))
    center1_y = int(center_y + radius1 * math.sin(angle1))
    center2_x = int(center_x + radius1 * math.cos(angle2))
    center2_y = int(center_y + radius1 * math.sin(angle2))
    center3_x = int(center_x + radius1 * math.cos(angle3))
    center3_y = int(center_y + radius1 * math.sin(angle3))

    axesLength = (28, 48)

    rot = angle
    rot1 = angle + 120
    rot2 = angle + 240

    cv2.ellipse(image, (center1_x, center1_y), axesLength, rot, 0, 360, (0, 0, 255), 2)
    cv2.ellipse(image, (center2_x, center2_y), axesLength, rot1, 0, 360, (255, 0, 0), 2)
    cv2.ellipse(image, (center3_x, center3_y), axesLength, rot2, 0, 360, (255, 0, 0), 2)

    name = imagename + f'_wheel_{point}_{angle0}.png'
    cv2.imwrite(name, image)
    return ((center1_x, center1_y), (center2_x, center2_y), (center3_x, center3_y))

