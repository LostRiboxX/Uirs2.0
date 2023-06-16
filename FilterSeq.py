import cv2
import numpy as np

img = cv2.imread('1.jpg_croped.png')


blur = cv2.medianBlur(img, 31)

image = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

pixel_vals = image.reshape((-1, 3))
cv2.imwrite('blur.png', img)

pixel_vals = np.float32(pixel_vals)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100000, 0)
k = 18
retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 18, cv2.KMEANS_RANDOM_CENTERS)
centers = np.uint8(centers)
segmented_data = centers[labels.flatten()]
segmented_image = segmented_data.reshape((image.shape))
img = cv2.cvtColor(segmented_image, cv2.COLOR_RGB2BGR)

for i in range(img.shape[0]):
    for j in range(img.shape[1]-1):
        if ((img[i,j][0] + img[i,j][1] + img[i,j][2]) - (img[i,j+1][0]+img[i,j+1][1]+img[i,j+1][2])) >= 10:
            img[i,j] = (0,0,0)
        else:
            img[i, j] = (255, 255, 255)

cv2.imwrite('diff.png', img)