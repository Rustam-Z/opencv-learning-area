import cv2

# Read image
img = cv2.imread("img/elon.png") # Translates to cv::Mat object
cv2.imshow('Elon', img)
cv2.waitKey(0)

# Read video 
capture = cv2.VideoCapture("img/cars.mp4")
while True:
    ret, frame = capture.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video", gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()