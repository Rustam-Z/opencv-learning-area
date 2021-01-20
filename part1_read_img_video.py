# Read images, videos, webcam

import cv2
from pip._vendor import urllib3

"""Open an image"""
# img = cv2.imread("media/192524.jpg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

"""Play a video"""
# cap = cv2.VideoCapture("media/Manage.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

"""Using with WebCam of Laptop"""
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

"""IP WebCam"""
# url = 'https://192.168.100.155:8080/video'
# cap = cv2.VideoCapture(url)
# cap.set(3, 640)
# cap.set(4, 480)
#
# while True:
#     ret, frame = cap.read()
#     if frame is not None:
#         cv2.imshow('frame', frame)
#     q = cv2.waitKey(1)
#     if q == ord("q"):
#         break
# cv2.destroyAllWindows()
