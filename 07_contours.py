# https://docs.opencv.org/master/d3/d05/tutorial_py_table_of_contents_contours.html

import cv2 as cv
import numpy as np

img = cv.imread('img/lp.png')
cv.imshow('Original', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # cv.CHAIN_APPROX_NONE
print(f'{len(contours)} contour(s) found!')

# cnt = contours[4]
# cv.drawContours(img, [cnt], 0, (0,255,0), 3)

cv.drawContours(blank, contours, -1, (0,0,255), 1) # draw all = -1
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)