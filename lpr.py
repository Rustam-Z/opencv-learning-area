import cv2
import numpy as np 

image_path = "img/lp1.png"

img = cv2.imread(image_path) 
cv2.imshow('Original', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resized_img = cv2.resize(gray_img, (300, 100), fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized_img)
print(resized_img.shape)

median = cv2.blur(resized_img, (5,5))
cv2.imshow('medianBlur', median)

blurred = cv2.GaussianBlur(median,(3,3),-1)
cv2.imshow('Gaussian Blur', blurred)

th = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,23,6)
cv2.imshow("Threshold", th)

cv2.waitKey(0)