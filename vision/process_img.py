import cv2
import numpy as np

def process_img(img):
    #essentially, this func returns the x coordinate of the center of the taped line OR if no line found, returns none

    #turn it to gray, blur, etc
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #sets boundaries of the color blue to use in masking
    lower_blue = np.array([80,60,40])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    mblur = cv2.medianBlur(mask, 5)
    gblur = cv2.GaussianBlur(mblur, (5,5), 0)
    _, thresh = cv2.threshold(gblur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    #code blow finds x coordinate of center of taped line
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea) #finds largest object based on contour area

        cv2.drawContours(thresh, [largest], -1, (0, 255, 0), 3)

        M = cv2.moments(largest)
        cx = int(M["m10"] / M["m00"]) #cx = coordinate x

        return cx

    else:
        print("No line detected.") 
        return None





