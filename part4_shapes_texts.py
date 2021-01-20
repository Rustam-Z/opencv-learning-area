import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # picture in opencv represents a numpy array
# print(img)
# img[:] = (255, 120, 0)  # changing the color

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)  # args: img, starting_point, ending_point, color, thickness

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
