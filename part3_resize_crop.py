import cv2
import numpy as np

img = cv2.imread("media/192524.jpg")
print(img.shape)

img_resize = cv2.resize(img, (200, 200))

# Crop the image
img_cropped = img[0:200, 200:500]  # y:y+h, x:x+w

cv2.imshow("Image", img)
cv2.imshow("Resized Image", img_resize)
cv2.imshow("Cropped Image", img_cropped)

cv2.waitKey(0)
