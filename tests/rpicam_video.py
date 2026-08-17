import time
from picamera2 import Picamera2

cam = Picamera2()
cam.start()

config = cam.create_video_configuration(
    main={"size": (1280, 720)},
    controls={"FrameRate": 30}
)
cam.configure(config)

filename = "rpi_video_081626.mp4"
cam.start_recording(filename)
print(f"Recording started. Saving to {filename}...")

time.sleep(10)

cam.stop_recording()

cam.close()