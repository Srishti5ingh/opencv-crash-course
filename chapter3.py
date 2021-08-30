#Chapter 3 = Resizing and cropping

import cv2
import numpy as np

img = cv2.imread("resources/jag.jpg")
print(img.shape)

imgResize = cv2.resize(img, (400, 200))         # Width - Height
imgCropped = img[0:200, 200:500]    # Height - Weight

cv2.imshow("Image", img)
cv2.imshow("Resized image", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
