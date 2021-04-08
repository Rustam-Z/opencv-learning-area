# Find rectangle, area is the bigggest
# Crop the area with partcular color
# USE ocr to extract text, until 'Select one:' or 'Answer:'
# If 'Select one:' select that one which is with "BLUE DOT"

import numpy as np
import cv2
import glob
import pytesseract

def crop_rectangles():
    for filename in glob.glob(r'*.jpg'):

        img = cv2.imread(filename)
        imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        ret, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
        contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


        for contour in contours:
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
            cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
            x = approx.ravel()[0]
            y = approx.ravel()[1] - 5
            
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                area = h * w
                if area >= 155000:
                    crop_img = img[y:y+h, x:x+w].copy() 
                    cv2.imshow("cropped", crop_img)
                    cv2.imwrite(f'cropped/{filename}', crop_img)
                    cv2.waitKey(0)
                
                
    #else:
        #cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    # cv2.imshow('Rect', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
 
 

for filename in glob.glob(r'test/*.jpg'):
    image = cv2.imread(filename)
    image = image[y:y+h, x:x+w]
    #image = cv2.resize(image, (0,0), fx=1, fy=1)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

    data = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    print(data)
    
    

    cv2.imshow('result', image)
    cv2.waitKey()
