import numpy as np
import cv2


def erase_subs(img):
    # img = cv2.imread("/home/alan/cap3.jpg", cv2.IMREAD_COLOR)
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cropped = greyscale[595:680, 254:1030].copy()

    _, thresholded = cv2.threshold(cropped, 200, 255, cv2.THRESH_BINARY)

    dilation_kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresholded, dilation_kernel, 1)

    cv2.imshow('dilation', dilated)

    cleaned = img.copy()
    cleaned[595:680, 254:1030] = cv2.inpaint(img[595:680, 254:1030], dilated, 5, cv2.INPAINT_TELEA)

    return cleaned
