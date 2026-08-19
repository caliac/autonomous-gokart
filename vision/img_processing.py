import cv2
import numpy as np
from pathlib import Path
from vision import line_detection

def process_vid(vid_path):

    processed_directory = Path(__file__).parent.parent / "processed_frames"
    processed_directory.mkdir(parents=True, exist_ok=True)

    vid = cv2.VideoCapture(str(vid_path))

    frame_num = 0

    while True:
        success, frame = vid.read()

        if not success:
            break

        prepared_frame = process_img(frame)
        processed_frame = vertical_line(prepared_frame, line_detection.find_center_x(prepared_frame))

        processed_path = processed_directory / f"frame_{frame_num:04d}.jpg"
        cv2.imwrite(str(processed_path), processed_frame)

        frame_num += 1

    vid.release()

    print(f"Processed {frame_num} frames.")




def process_img(img):
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

def vertical_line(img, x):
    #pass in x coordinate and image; returns image with vertical green line drawn
    height, _, _ = img.shape

    startpt = (x, height)
    endpt = (x, 0)
    line_color = (0, 255, 0)
    line_thickness = 5
    
    cv2.line(img, startpt, endpt, line_color, line_thickness)

    return img



process_vid("/home/calia/autonomous-gokart/videos/video_08182026_211327.mp4")

