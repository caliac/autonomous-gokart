from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from datetime import datetime
import time
from pathlib import Path

def record_video(vid_length):

    vid_directory = Path(__file__).parent.parent / "videos"
    vid_directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%m%d%Y_%H%M%S")
    vid_path = vid_directory / f"video_{timestamp}.mp4"

    rpi_cam = Picamera2()

    config = rpi_cam.create_video_configuration()
    rpi_cam.configure(config)

    encoder = H264Encoder()
    output = FfmpegOutput(str(vid_path))

    rpi_cam.start()

    rpi_cam.start_recording(encoder, output)
    print("Starting video recording.")
    time.sleep(vid_length)

    rpi_cam.stop_recording()

    print(f"Video recorded for {vid_length} seconds. Saved to {vid_path}.")

    rpi_cam.close()

    return vid_path



seconds = 10
record_video(seconds)