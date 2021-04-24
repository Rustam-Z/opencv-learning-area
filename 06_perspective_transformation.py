import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('img/lp6.png')
cv.imshow("Original", img)
rows, cols, ch = img.shape

print(">>", rows, cols, ch)
pts1 = np.float32([[6,15],[40,15],[75,200],[125,195]])
pts2 = np.float32([[0,0],[40,0],[0,180],[40,180]])

M = cv.getPerspectiveTransform(pts1,pts2)

dst = cv.warpPerspective(img,M,(180,40))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

cv.waitKey(0)