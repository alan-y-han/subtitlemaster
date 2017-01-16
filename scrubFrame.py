import numpy as np
import cv2


def scrubsubs(img):
    img = cv2.imread("/home/alan/cap3.jpg", cv2.IMREAD_COLOR)
    greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cropped = greyscale[595:680, 254:1030].copy()

    _, thresholded = cv2.threshold(cropped, 200, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)

    dilated = cv2.dilate(thresholded, kernel, 1)

    img1 = img.copy()
    # img2 = img.copy()
    # img3 = img.copy()
    # img4 = img.copy()
    # img5 = img.copy()

    # img1[595:680, 254:1030] = cv2.inpaint(img[595:680, 254:1030], dilated, 10, cv2.INPAINT_NS)
    img1[595:680, 254:1030] = cv2.inpaint(img[595:680, 254:1030], dilated, 10, cv2.INPAINT_TELEA)
    # img3[595:680, 254:1030] = cv2.inpaint(img[595:680, 254:1030], dilated, 2, cv2.INPAINT_TELEA)
    # img4[595:680, 254:1030] = cv2.inpaint(img[595:680, 254:1030], dilated, 3, cv2.INPAINT_TELEA)
    # img5[595:680, 254:1030] = cv2.inpaint(img[595:680, 254:1030], dilated, 4, cv2.INPAINT_TELEA)

    # greyscale[595:680, 254:1030] = dilated

    # cv2.imshow('cropped', cropped)
    # cv2.imshow('thresholded', thresholded)
    # cv2.imshow('dilated', dilated)
    # cv2.imshow('img', img)
    # cv2.imshow('img1', img1)
    # cv2.imshow('img2', img2)
    # cv2.imshow('img3', img3)
    # cv2.imshow('img4', img4)
    # cv2.imshow('img5', img5)

    return img1

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
