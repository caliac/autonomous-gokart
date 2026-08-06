#finds line, returns center (ex. 210)

import cv2

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