#https://www.helmholtz-hida.de/en/events/translate-to-englisch-helmholtz-gpu-hackathon-2022/
import numpy as np
import cv2

video = cv2.VideoCapture(0)

upper_blue = np.array([130,255,255])

lower_green = np.array([40 , 100 , 20])
upper_green = np.array([75 , 250 , 255])

lower_red = np.array([0,150 ,20])
upper_red = np.array([15 ,255,255])

while video.isOpened():
    _,blueIMG = video.read()
    _,redIMG = video.read()
    image = cv2.cvtColor(blueIMG,cv2.COLOR_BGR2HSV)

    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)


    cv2.waitKey(1)

cv2.destroyAllWindows()
