import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    for i in range(100):
        camera.brightness = i
        time.sleep(0.2)
    camera.stop_preview()