#camera class

import time
import libcamera
from picamera2 import Picamera2

cam = Picamera2()

config = cam.create_preview_configuration(
    transform=libcamera.Transform(hflip=1, vflip=1)
)
cam.configure(config)

cam.start()

time.sleep(2)

cam.capture_file("myPhoto3.jpg")
print("image captured.")

cam.close()