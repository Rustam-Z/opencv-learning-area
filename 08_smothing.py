import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('img/lp.png')

# Averaging
average = cv.blur(img, (5,5))

# GaussianBlur
gauss = cv.GaussianBlur(img,(5,5),0)

# Median blur
median = cv.medianBlur(img,3)

# Bilateral Filtering
bilaterial15 = cv.bilateralFilter(img,9,15,15) # src, d, sigmaColor, sigmaSpace 
bilaterial75 = cv.bilateralFilter(img,100,75,75) # src, d, sigmaColor, sigmaSpace 

plt.subplot(2,3,1),plt.imshow(img),plt.title('Original')
plt.subplot(2,3,2),plt.imshow(average),plt.title('Blurred')
plt.subplot(2,3,3),plt.imshow(gauss),plt.title('Gaussian')
plt.subplot(2,3,4),plt.imshow(median),plt.title('Median')
plt.subplot(2,3,5),plt.imshow(bilaterial15),plt.title('Bilateral 15')
plt.subplot(2,3,6),plt.imshow(bilaterial75),plt.title('Bilateral 75')

plt.show()

"""
# Image Filtering
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
"""