from cv2 import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("Track Bars")
cv2.resizeWindow("Track Bars", (640, 240))
cv2.createTrackbar("Hue Min", "Track Bars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Value Min", "Track Bars", 0, 255, empty)
cv2.createTrackbar("Value Max", "Track Bars", 255, 255, empty)

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat Min", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat Max", "Track Bars")
    v_min = cv2.getTrackbarPos("Value Min", "Track Bars")
    v_max = cv2.getTrackbarPos("Value Max", "Track Bars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Original Image", img)
    cv2.imshow("Final Output", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break