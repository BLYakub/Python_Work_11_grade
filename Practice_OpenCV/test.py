from cv2 import cv2
import numpy as np

# Image
# RGB
# img = cv2.imread("starry_night.jpg", cv2.IMREAD_COLOR)

# # Grayscale
# img = cv2.imread("starry_night.jpg", cv2.IMREAD_GRAYSCALE)

# # Print image
# cv2.imshow("Starry Night", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Video

# cap = cv2.VideoCapture("test_video.mp4")

# while True:
#     success, img = cap.read()
#     if not success:
#         break
#     cv2.imshow("Video", img)
#     cv2.waitKey(1)


# Webcam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

success, img = cap.read()

cv2.imshow("Picture", img)
cv2.waitKey(0)


# Converting image colors and blurring

# img = cv2.imread('starry_night.jpg')
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (9,9), 0)
#
# cv2.imshow("Starry Night", imgGray)
# cv2.imshow("Blurry Starry Night", imgBlur)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Canny/dilate/erode images

# img = cv2.imread('lena.png')
# kernel = np.ones((5,5), np.uint8)
#
# imgCanny = cv2.Canny(img, 100, 100)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
#
#
# cv2.imshow("Canny image", imgCanny)
# cv2.imshow("Dilated image", imgDilation)
# cv2.imshow("Eroded image", imgEroded)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Resizing images

# img = cv2.imread('dog.jpg')
# print(img.shape)
#
# imgResize = cv2.resize(img, (500, 200))
# print(imgResize.shape)
#
# imgCropped = img[0:200, 50:200]
# print(imgCropped.shape)
#
# cv2.imshow('Dog image', img)
# cv2.imshow('Resized Dog image', imgResize)
# cv2.imshow('Cropped Dog image', imgCropped)
# cv2.waitKey(0)


# Coloring images

# img = np.zeros((512, 512, 3), np.uint8)

img = cv2.imread('lena.png')

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 70), 50, (255, 255, 0), 5)
cv2.putText(img, 'HELLO', (300, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255))

cv2.imshow("Image", img)
cv2.waitKey(0)


# Detect colors

# img = cv2.imread('pokemon.png')
#
# boundaries = [
#     ([17, 15, 100], [50, 56, 200]),
#     ([86, 31, 4], [220, 88, 50]),
#     ([25, 146, 190], [62, 174, 250]),
#     ([103, 86, 65], [145, 133, 128])
# ]
#
# for (lower, upper) in boundaries:
#     # create NumPy arrays from the boundaries
#     lower = np.array(lower, np.uint8)
#     upper = np.array(upper, np.uint8)
#     # find the colors within the specified boundaries and apply
#     # the mask
#     mask = cv2.inRange(img, lower, upper)
#     output = cv2.bitwise_and(img, img, mask=mask)
#     # show the images
#     cv2.imshow("images", np.hstack([img, output]))
#     cv2.waitKey(0)


# Detecting Shapes

# def get_contours(img):
#     contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
#         peri = cv2.arcLength(cnt, True)
#         print(peri)
#         approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
#         print(len(approx))
#         objCor = len(approx)
#         x, y, w, h = cv2.boundingRect(approx)
#
#         if objCor == 3:
#             objectType = "Tri"
#         elif objCor == 4:
#             objectType = "Squa"
#         elif objCor > 4:
#             objectType = "Circ"
#         else:
#             objectType = "None"
#
#         cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#
# img = cv2.imread('shapes.png')
# imgContour = img.copy()
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
# imgCanny = cv2.Canny(imgBlur, 50, 50)
# get_contours(imgCanny)
#
# cv2.imshow("Image", img)
# # cv2.imshow("Gray", imgGray)
# # cv2.imshow("Blur", imgBlur)
# # cv2.imshow("Canny", imgCanny)
# cv2.imshow("Contour", imgContour)
# cv2.waitKey(0)

# img = cv2.imread('shapes.png')
# imgContour = img.copy()
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
# imgCanny = cv2.Canny(imgBlur, 100, 100)
#
# contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     print("area: " + str(area))
#     if area > 500:
#         cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
#         para = cv2.arcLength(cnt, True)
#         print("perimeter: " + str(para))
#         approx = cv2.approxPolyDP(cnt, 0.02*para, True)
#         print("approximate points: " + str(len(approx)))
#
#         objCor = len(approx)
#         x, y, w, h = cv2.boundingRect(approx)
#
#         if objCor == 3:
#             objectType = "Tri"
#         elif objCor == 4:
#             if 0.95 < float(w / h) < 1.05:
#                 objectType = "Square"
#             else:
#                 objectType = "Rectangle"
#         elif objCor > 4:
#             objectType = "Circle"
#         else:
#             objectType = "None"
#
#         cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
#         cv2.putText(imgContour, objectType, (x+(w//2)-20, y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#
# cv2.imshow("Contour Detection", imgContour)
# cv2.waitKey(0)


# Facial detection

# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#
# img = cv2.imread("leo.jpg")
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 39)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv2.putText(img, "LEO", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
#     cv2.imshow("Face Detection", img)
#
# cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
#
# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# while True:
#     success, img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     faces = faceCascade.detectMultiScale(imgGray, 1.1, 39)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.putText(img, "CUTE", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 1)
#     cv2.imshow("Output", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# Painter with color detection

# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
#
# # [min_hue, min_sat, min_val, max_hue, max_sat, max_val]
# my_colors = [
#     [73, 73, 0, 98, 255, 255],  # Green
#     [107, 96, 0, 122, 255, 255],  # Blue
#     [22, 74, 0, 31, 156, 255]  # Yellow
# ]
#
# # [B, G, R]
# color_values = [
#     [7, 199, 0],  # Green
#     [204, 0, 0],  # Blue
#     [0, 255, 255]  # Yellow
# ]
#
# my_points = []
#
#
# def find_color(img, my_colors):
#     img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     index_colors = 0
#     new_points = []
#     for color in my_colors:
#         lower = np.array(color[:3])
#         upper = np.array(color[3:])
#         mask = cv2.inRange(img_HSV, lower, upper)
#         cv2.imshow("mask", mask)
#         x, y = get_contours(mask)
#         if x != 0 and y != 0:
#             # cv2.circle(img, (x, y), 10, color_values[index_colors], cv2.FILLED)
#             new_points.append([x, y, index_colors])
#         index_colors += 1
#     return new_points
#
#
# def get_contours(mask):
#     contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
#     x, y, w, h = 0, 0, 0, 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:
#             # cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
#             para = cv2.arcLength(cnt, True)
#             approx = cv2.approxPolyDP(cnt, 0.02*para, True)
#             x, y, w, h = cv2.boundingRect(approx)
#     return x, y
#
#
# def draw_on_canvas():
#     for point in my_points:
#         cv2.circle(img, (point[0], point[1]), 10, color_values[point[2]], cv2.FILLED)
#
#
# while True:
#     success, img = cap.read()
#     img = cv2.flip(img, 1)
#     new_points = find_color(img, my_colors)
#
#     if len(new_points) != 0:
#         for new_p in new_points:
#             my_points.append(new_p)
#     if my_points != 0:
#         draw_on_canvas()
#
#     cv2.imshow("Result", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
