import numpy as np
import cv2

x_start = 254
x_end = 1030
y_start = 595
y_end = 680


def erase_subs(img):
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cropped = greyscale[y_start:y_end, x_start:x_end].copy()

    _, thresholded = cv2.threshold(cropped, 200, 255, cv2.THRESH_BINARY)

    dilation_kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresholded, dilation_kernel, 1)

    cv2.imshow('dilation', dilated)

    cleaned = img.copy()
    cleaned[y_start:y_end, x_start:x_end] = cv2.inpaint(img[y_start:y_end, x_start:x_end], dilated, 5,
                                                        cv2.INPAINT_TELEA)

    return cleaned
