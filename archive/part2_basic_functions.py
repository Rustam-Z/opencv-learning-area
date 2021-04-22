import cv2
import numpy as np

img = cv2.imread("media/192524.jpg")
kernel = np.ones((5, 5), np.uint8)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to gray
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
img_canny = cv2.Canny(img, 100, 100)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)  # make the edges large
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)  # make the edges thicker

# cv2.imshow("Gray Image", img_gray)
# cv2.imshow("Blur Image", img_blur)
# cv2.imshow("Canny Image", img_canny)
cv2.imshow("Image Dilation", img_dilation)
cv2.imshow("Image Erosion", img_eroded)

cv2.waitKey(0)
