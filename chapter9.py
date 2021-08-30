# Chapter 9: Face Detection

import cv2

faceCascade =cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img = cv2.imread("resources/profile.jpeg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img,(x,y), (x+w, y+h), (0, 255, 0), 8)


cv2.imshow("results", img)
cv2.waitKey(0)