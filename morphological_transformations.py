import cv2 as cv
import numpy as np

# 1. Erosion
img = cv.imread('img/elon.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)

# 2. Dilation
dilation = cv.dilate(img,kernel,iterations = 1)

# 3. Opening - dots
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# 4. Closing
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

# 5. Morphological Gradient
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# 6. Top Hat & black hat
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

# blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

"""
# Rectangular Kernel
>>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
"""