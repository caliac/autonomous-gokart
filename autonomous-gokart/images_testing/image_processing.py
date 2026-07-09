#test file

import cv2
import numpy as np

img = cv2.imread('images_testing/blueTape.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#sets boundaries of the color blue
lower_blue = np.array([80,60,40])
upper_blue = np.array([130,255,255])

#mask = everything blue
mask = cv2.inRange(hsv, lower_blue, upper_blue)

mblur = cv2.medianBlur(mask, 5)
final_blur = cv2.GaussianBlur(mblur, (5,5), 0)
(retval, thresh) = cv2.threshold(final_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


#when program is run, image appears in a popup, press any keyboard key to close it
#cv2.imshow('hsv version', hsv)
cv2.imshow('mask', mask)
cv2.imshow('med+gaus blur', final_blur)
#cv2.imshow('image', img)
cv2.imshow('thresh result', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()