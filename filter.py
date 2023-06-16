import cv2
import numpy as np


def filter(imgname):

    img = cv2.imread(imgname)


    blur = cv2.medianBlur(img, 31)

    image = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    pixel_vals = image.reshape((-1, 3))

    pixel_vals = np.float32(pixel_vals)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100000, 0)
    k = 18
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 18, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    segmented_image = segmented_data.reshape((image.shape))
    img = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR)

    cv2.imwrite(imgname + "_filtered.png", img)
    return imgname + "_filtered.png"