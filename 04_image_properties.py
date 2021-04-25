# https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
import numpy as np
import cv2 

img = cv2.imread('img/elon.png')

"""Accessing and Modifying pixel values"""
px = img[100, 100] # access the pixel value
print(px)

img[100,100] = [0,255,0] # modifying the pixel value OR img.itemset((100, 100, 2), 100) for RED channel
print(img[100, 100]) # OR img.item(10,10,2) for RED channel

"""Image properties"""
print(">> shape", img.shape)
print(">> size", img.size)
print(img.dtype)

"""Image ROI = Region of interest"""
crop = img[300:500, 400:600] # [y1:y2, x1:x2], first height then width, select area in image

img[400:600, 100:300] = crop
cv2.imshow("ROI", img)

"""Splitting and Merging Image Channels"""
# b,g,r = cv2.split(img) 
# merged = cv2.merge([b, g, r])
b = img[:,:,0] # Blue, "Select BLUE channel within the full HEIGHT and WIDTH of image"
g = img[:,:,1] # Green
r = img[:,:,2] # Red

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

img[:,:,2] = 0 # Set all the red pixels to zero
# img[:,:,1] = 0 # Set all green to zero
cv2.imshow("Without red", img)

cv2.waitKey(0)