import cv2

path = 'img/2.png'

originalImage = cv2.imread(path)
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
whiteImage = cv2.subtract(255, grayImage)

(thresh, blackAndWhiteImage) = cv2.threshold(whiteImage, 127, 255, cv2.THRESH_BINARY)
 
cv2.imwrite('img/3.png', whiteImage)

#cv2.imshow('Black white image', blackAndWhiteImage)
#cv2.imshow('Original image',originalImage)
#cv2.imshow('Gray image', grayImage)
cv2.imshow('White image', whiteImage) # will be used


cv2.waitKey(0)
cv2.destroyAllWindows()