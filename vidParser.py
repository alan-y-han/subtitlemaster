import numpy as np
import cv2
import ScrubFrame

cap = cv2.VideoCapture('/home/alan/idolmaster/part1.mp4')

# vwriter = cv2.VideoWriter('/home/alan/idolmaster_test.mp4',
#                           cv2.VideoWriter_fourcc(*'X264'),
#                           30,
#                           (1280, 720))

counter = 0

while cap.isOpened():
    counter += 1

    _, frame = cap.read()

    cleanedFrame = ScrubFrame.erase_subs(frame)

    # cv2.imshow('ori frame', frame)
    # cv2.imshow('clean frame', cleanedFrame)
    # cv2.waitKey(0)
    cv2.imwrite('/media/alan/Transcend/temp/frame' + str(counter) + '.png', cleanedFrame)

    # if counter > 10:
    #     break

cap.release()
cv2.destroyAllWindows()
