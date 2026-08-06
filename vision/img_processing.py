import cv2
import numpy as np

def process_img(img):
    #converts img to hsv, masks, blurs, thresholds; returns the img to pass into find_center()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #sets boundaries of the color blue to use in masking
    lower_blue = np.array([80,60,40])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    mblur = cv2.medianBlur(mask, 5)
    gblur = cv2.GaussianBlur(mblur, (5,5), 0)
    _, thresh = cv2.threshold(gblur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return thresh

def vertical_line(img, x):
    #pass in x coordinate and image; returns image with vertical green line drawn
    height, _, _ = img.shape

    startpt = (x, height)
    endpt = (x, 0)
    line_color = (0, 255, 0)
    line_thickness = 5
    
    cv2.line(img, startpt, endpt, line_color, line_thickness)

    return img

