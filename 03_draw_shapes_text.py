# https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html

import cv2
import numpy as np 

blank = np.zeros((500, 500, 3), dtype='uint8')
blank1 = np.zeros((500, 500, 3), dtype='uint8')
cv2.imshow("Blank", blank)

# 1. Paint the whole image a particular color
blank[:, 100:300] = (0, 0, 255) # Blue, Green, Red
cv2.imshow("Green", blank)

# 2. Draw a rectangle
cv2.rectangle(blank, (5, 0), (50, 150), (0, 0, 255), thickness=-1) # (img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
# Or alternatively ```cv2.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=cv2.FILLED)```
cv2.imshow("Rectangle", blank)

# 3. Draw a circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 0), thickness=3) # (img, center, radius, color, thinkness=None, lineType=None, shift=None)
cv2.imshow("Circle", blank)

# 4. Draw a line
cv2.line(blank1, (0, 250), (blank1.shape[1]//2, blank1.shape[0]//2), (255, 255, 255), thickness=3)
cv2.imshow("Line", blank1)

# 5. Write a text on image
cv2.putText(blank1, "Hello Mars!", (250, 250), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2)
cv2.imshow("Text", blank1)

cv2.waitKey(0)