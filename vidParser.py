import numpy as np
import cv2
import scrubFrame

cap = cv2.VideoCapture('/home/alan/idolmaster/part1.mp4')

while cap.isOpened():
    _, frame = cap.read()

    cv2.imshow('frame', frame)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
