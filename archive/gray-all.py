import cv2
import glob

for filename in glob.glob(r'img\*.png'):
    print(filename)
    img=cv2.imread(filename) 
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    whiteImage = cv2.subtract(255, grayImage)
    
    cv2.imwrite(f'{filename}', whiteImage)