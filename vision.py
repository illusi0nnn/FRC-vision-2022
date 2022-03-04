#https://www.helmholtz-hida.de/en/events/translate-to-englisch-helmholtz-gpu-hackathon-2022/
import numpy as np
import cv2

video = cv2.VideoCapture(0)
lower_blue = np.array([100,140,20])
upper_blue = np.array([130,255,255])

lower_red = np.array([0,150 ,20])
upper_red = np.array([15 ,255,255])

while True:
    _,img = video.read()
    image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(image,lower_blue,upper_blue)
    #mask = cv2.inRange(image,lower_red, upper_red)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for i in contours:
            x, y, w, h = cv2.boundingRect(i)
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),3)

    cv2.imshow('mask',mask)
    cv2.imshow('webcame', img)

    cv2.waitKey(1)
