from picamera2 import Picamera2
from . import process_img
from . import steering_error

def capture(cam):

    config = cam.create_preview_configuration({'format': 'BGR888'})
    cam.configure(config)
    cam.start()
    
    img = cam.capture_array()
        
    steering_error = steering_error(process_img(img))
    #will convert the colors -> find centroid -> find center x=line

    cam.close()

    return steering_error