"""
#coordinates of all the other files, basic structure
import vision
import cv2

#for the final main.py, i won't need to print all of this stuff. all these lines are just for testing purposes only.
image = cv2.imread('/Users/caliachau/Documents/GitHub/autonomous-gokart/autonomous-gokart/media/BlueTapeDrawing.png')

prepared_img = vision.img_processing.process_img(image)
x_val = vision.line_detection.find_center_x(prepared_img)
print(f"X Coordinate of Center Line: {x_val}")
img_with_center = vision.img_processing.vertical_line(image, x_val)

cv2.imshow("Image with Center Line Drawn", img_with_center)

steering_error = vision.steering_error.calc_steering_error(x_val)

if steering_error > 0:
    print(f"Steer {steering_error} pixels to the right.")
elif steering_error < 0:
    print(f"Steer {abs(steering_error)} pixels to the left.")
else: #steering error = 0; on target
    print(f"Steering is on target at {steering_error} pixels.")

#when program is run, image appears in a popup, press any keyboard key to close it
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

import time
import hardware

my_driver = hardware.motor_driver.MotorDriver(RPWMpin=18, LPWMpin=19, R_ENpin=23, L_ENpin=24)
my_motor = hardware.motor.Motor(my_driver)

try:

    my_motor.set_speed(10)
    time.sleep(2)
    my_motor.set_speed(70)
    time.sleep(2)
    my_motor.set_speed(0)
    time.sleep(2)
    my_motor.set_speed(-50)
    time.sleep(2)
    my_motor.set_speed(-100)
    time.sleep(2)
    my_motor.set_speed(-30)
    time.sleep(2)
    my_motor.set_speed(0)

except KeyboardInterrupt: #press ctrl c to quit
    my_motor.set_speed(0)

finally:
    my_driver.end()
