import cv2
import numpy
from PIL import Image, ImageOps

def imgContours(imgname):
    img = cv2.imread(imgname)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]-1):
            if ((img[i,j][0] + img[i,j][1] + img[i,j][2]) - (img[i,j+1][0]+img[i,j+1][1]+img[i,j+1][2])) >= 10:
                img[i,j] = (0,0,0)
            else:
                img[i, j] = (255, 255, 255)

    eroded = cv2.erode(img, None, iterations=15)
    cv2.imwrite('differosed.jpg', eroded)
    ImageOps.expand(Image.open('differosed.jpg'), border=3, fill='black').save('differosed.jpg')
    img = cv2.imread('differosed.jpg')

    _, thresh = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)
    cv2.imwrite(imgname + "_contours.png", thresh)
    return (imgname + "_contours.png")