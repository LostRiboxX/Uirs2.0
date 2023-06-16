import cv2


def croped(imgname):
    img = cv2.imread(imgname)
    cropped_image = img[0:1025, 370:1400]
    cv2.imwrite(imgname + "_croped.png", cropped_image)
    return imgname + "_croped.png"
