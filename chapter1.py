# Chapter 1 consists of following:
# Intro to CV
# Installation of OpenCV packages
# Read images, videos and Webcam

#Module 1
#import cv2
#print("Package Imported")



#Module 2 : Read Images
#img = cv2.imread("resources/cat.png")
#cv2.imshow("output", img)
#cv2.waitKey(0)



#Module 3 : Read Web Cam

import cv2
#cap = cv2.VideoCapture("resources/nik.mp4")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break