import numpy as np
import cv2
import ScrubFrame

video_in = cv2.VideoCapture('/home/alan/idolmaster/part1.mp4')

video_out = cv2.VideoWriter('/home/alan/idolmaster_test.mp4',
                            cv2.VideoWriter_fourcc(*'X264'),
                            30,
                            (1280, 720))

counter = 0

# no_frames = cap.get(cv2.)

while video_in.isOpened():
    ret, frame = video_in.read()

    if ret:
        counter += 1
        cleanedFrame = ScrubFrame.erase_subs(frame)

        # cv2.imwrite('/media/alan/Transcend/temp/frame' + str(counter) + '.png', cleanedFrame)
        video_out.write(cleanedFrame)
        print('Processed frame ' + str(counter))
    else:
        break

video_in.release()
video_out.release()
cv2.destroyAllWindows()
