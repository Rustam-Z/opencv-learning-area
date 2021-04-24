# https://docs.opencv.org/master/da/d6e/tutorial_py_geometric_transformations.html
# Perspective transformation is also there

import cv2
import numpy as np 

img = cv2.imread("img/elon.png")

cv2.imshow("Elon", img)

def translate(img, x, y): # shifting to (x, y)
    # -x = left | -y = up | x = right | y = down
    trans_matrix = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # height, width
    return cv2.warpAffine(img, trans_matrix, dimensions)

translated = translate(img, 100, 200)
cv2.imshow("Translated", translated)

def rotation(img, angle, rot_point=None):
    (height, width) = img.shape[:2]

    if rot_point is None:
        rot_point = (width//2, height//2)

    rot_matrix = cv2.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rot_matrix, dimensions)

rotated = rotation(img, 45,)
cv2.imshow("Rotated", rotated)

# Flip
flip = cv2.flip(img, 1) # -1=mirror+ivert, 0=invert, 1=mirror
cv2.imshow("Flipped", flip)

cv2.waitKey(0)

"""
1. Erosion
img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)

2. Dilation
dilation = cv.dilate(img,kernel,iterations = 1)

3. Opening - dots
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

4. Closing
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

5. Morphological Gradient
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

6. Top Hat
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

7. Black Hat
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