#calculates steering error based on line center and image center (ex. -30)
import constants

def calc_steering_error(line_center):
    img_center = (constants.width) / 2
    steering_error = line_center - img_center
    #positive value = line to the right = steer to the right
    #negative value = line to the left = steer to the left

    return steering_error