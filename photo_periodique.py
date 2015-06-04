import time
import picamera
import datetime

VIDEO_DAYS = 720
FRAMES_PER_HOUR = 6
FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS

def capture_frame(frame):
    with picamera.PiCamera() as cam:
	cam.resolution = (1920,1080)
		cam.awb_mode = 'horizon'
        time.sleep(2)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H-%M-%S')
        cam.capture('/home/pi/Camera/frame %s.jpg' % st)

for frame in range(FRAMES):
    start = time.time()
    capture_frame(frame)
    time.sleep(int(60*60/FRAMES_PER_HOUR) - (time.time() - start))
    
