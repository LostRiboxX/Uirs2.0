import cv2
import numpy as np



def drawconts(imgnamecont, imagename):
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



                cv2.drawContours(image, [i[0]-200,i[1]-200], -1, (0, 255, 0), 2)
                cv2.circle(image, (cx+5, cy-5), 10, (0, 0, 255), -1)
                cv2.putText(image, str(j),(cx-10, cy-10), font, fontScale, fontColor, thickness, lineType)
                massx = ["cx brown", cx,"cy brown: ", cy]
                mass1 = [cx - 5,cy - 5]
                massbrown.append(mass1)
                contsmass.append(i)
                j += 1


    cv2.imwrite(imagename + "_done.png", image)
    return massbrown, contsmass