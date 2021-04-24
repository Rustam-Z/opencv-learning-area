# https://docs.opencv.org/master/d2/d96/tutorial_py_table_of_contents_imgproc.html

import cv2

img = cv2.imread("img/elon.png")
cv2.imshow('Elon', img)

# 1. Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# 2. Blur
# cv2.BORDER_DEFAULT: https://docs.opencv.org/master/d2/de8/group__core__array.html#ga209f2f4869e304c82d07739337eae7c5
blur = cv2.GaussianBlur(img, (7, 7), 0) 
cv2.imshow("Blur", blur)

# 3. Edge cascade
canny = cv2.Canny(blur, 125, 175)
cv2.imshow("Canny", canny)

# 4. Dilate the image
dilated = cv2.dilate(canny, (7, 7), iterations=3)
cv2.imshow("Dilated", dilated)

# 5. Eroding
eroded = cv2.erode(dilated, (3, 3), iterations=1)
cv2.imshow("Eroded", eroded)

# 6. Resize
resized = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized", resized)

# 7. Crop
cropped = img[100:400, 300:600]
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
