import vision
from picamera2 import Picamera2
from vision import capture

camera = Picamera2()

#for 10 seconds or smth
frames = 0
while frames < 30:
    steering_error = capture.capture(camera) #find a way to break/end the capture program
    print(steering_error)
    frames += 1