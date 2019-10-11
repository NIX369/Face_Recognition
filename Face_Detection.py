
#To Check whether face is beind detected

import numpy as np
import cv2
faceCascade = cv2.CascadeClassifier('Cascades\\haarcascade_frontalface_alt.xml')

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(3, 640)  # set Width
camera.set(4, 480)  # set Height
while (True):
    ret, frame = camera.read()
 #   cv2.imshow('frame', frame)
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.2,
        minNeighbors=5,
    )
    for (x, y, w, h) in faces:
        frames = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        cv2.imshow("Nikhil", frames)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break

camera.release()
cv2.destroyAllWindows()