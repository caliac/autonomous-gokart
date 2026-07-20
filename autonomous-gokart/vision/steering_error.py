#calculates steering error based on line center and image center (ex. -30)
import constants

def calc_steering_error(line_center): #center = center of the line, calculated from img_processing.py
    img_center = (constants.width) / 2
    steering_error = img_center - line_center

    return steering_error #positive value = steer right, negative value = steer left