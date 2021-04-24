# https://docs.opencv.org/master/da/d6e/tutorial_py_geometric_transformations.html

import cv2

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA) # cv.INTER_LINEAR & cv.INTER_CUBIC for zooming, INTER_AREA is for shrinking

capture = cv2.VideoCapture("img/cars.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame, scale=0.2) # Resize the frame

    cv2.imshow("Video", frame)
    cv2.imshow("Resized video", frame_resized)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()