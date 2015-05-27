import time
import picamera
from datetime import datetime, timedelta

def wait():
    # Calculate the delay to the start of the next hour
    next_hour = (datetime.now() + timedelta(minutes=1))
    delay = (next_hour - datetime.now()).seconds
    time.sleep(delay)

with picamera.PiCamera() as camera:
    camera.resolution = (1680,1050)
    # camera.start_preview()
    wait()
    for filename in camera.capture_continuous('/home/pi/camera/img {timestamp:%Y-%m-%d-%H-%M}.jpg'):
        print('Captured %s' % filename)
        wait()

