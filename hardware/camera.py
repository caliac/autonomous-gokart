
#camera class

import time
from picamera2 import Picamera2

cam = Picamera2()
cam.start()

time.sleep(2)

cam.capture_file("8-15-26 photo")
print("image captured.")

cam.close()