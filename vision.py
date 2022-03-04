#https://www.helmholtz-hida.de/en/events/translate-to-englisch-helmholtz-gpu-hackathon-2022/
import numpy as np
import cv2

video = cv2.VideoCapture(0)

if video.isOpened() != True:
    print("ERROR: can't open camera")

lower_blue = np.array([90,140,20])
upper_blue = np.array([130,255,255])

lower_red = np.array([0,150 ,20])
upper_red = np.array([15 ,255,255])

lower_green = np.array([40 , 100 , 20])
upper_green = np.array([75 , 250 , 255])

text = np.array(['blue', 'red'])

while video.isOpened():
    _,blueIMG = video.read()
    _,redIMG = video.read()
    image = cv2.cvtColor(blueIMG,cv2.COLOR_BGR2HSV)

    if len(blueContours) != 0 or len(redContours) != 0:
        for i in blueContours:
            x, y, w, h = cv2.boundingRect(i)
            if h*w >= 1350:
                cv2.rectangle(blueIMG, (x,y), (x+w, y+h), (255,0,0),3)
                cv2.putText(blueIMG, text[0], (x-(15*len(text[0])),y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1, cv2.LINE_AA)
                #this is for testing how we should handle the ball detection and its place on the screen
                #if width/2 - 55 < x and width/2 + 55 > x:
                #    print("B-> mid")
                #elif width/2 > x:
                #    print("B-> left")
                #else:
                #    print("B-> right")
        for i in redContours:
            x,y,w,h = cv2.boundingRect(i)
            if h*w >= 1350:
                cv2.rectangle(redIMG, (x,y), (x+w,y+h), (0,0,255), 3)
                cv2.putText(redIMG, text[1], (x-(15*len(text[1])),y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
                #this is for testing how we should handle the ball detection and its place on the screen
                #if width/2 - 55 < x and width /2 + 55 > x:
                #    print("R-> mid")
                #elif width/2 > x:
                #    print("R-> left")
                #else:
                #    print("R-> right")
    
    cv2.imshow('blue obj', blueIMG)
    cv2.imshow('red obj', redIMG)
    cv2.waitKey(1)

cv2.destroyAllWindows()