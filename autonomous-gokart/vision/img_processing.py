import cv2
import numpy as np

def prep_img(img):
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


def find_center_x(img):
    #returns the x coordinate of the center of the largest contour/object found

    contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea) #finds largest object based on contour area

        cv2.drawContours(img, [largest], -1, (0, 255, 0), 3)

        M = cv2.moments(largest)
        cx = int(M["m10"] / M["m00"])
        #cy = int(M["m01"] / M["m00"]) this finds y coordinate of center, but this isn't really needed (yet?) for steering

        return cx

    else:
        print("No contours/objects detected.")
        return None

def vertical_line(img, x):
    #pass in x coordinate and image; returns image with vertical green line drawn
    height, _, _ = img.shape

    startpt = (x, height)
    endpt = (x, 0)
    line_color = (0, 255, 0)
    line_thickness = 5
    
    cv2.line(img, startpt, endpt, line_color, line_thickness)

    return img


image = cv2.imread('/Users/caliachau/Documents/GitHub/autonomous-gokart/autonomous-gokart/media/BlueTapeDrawing.png')

prepared_img = prep_img(image)
x_val = find_center_x(prepared_img)
print(f"X Coordinate of Center Line: {x_val}")
img_with_center = vertical_line(image, x_val)

cv2.imshow("Image with Center Line Drawn", img_with_center)

#when program is run, image appears in a popup, press any keyboard key to close it
cv2.waitKey(0)
cv2.destroyAllWindows()
