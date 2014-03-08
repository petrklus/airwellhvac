import picamera
import io
import time
import picamera
from PIL import Image
"""
Tips mainly from http://picamera.readthedocs.org/en/release-1.2/recipes1.html
"""


# Create the in-memory stream
stream = io.BytesIO()

with picamera.PiCamera() as camera:
    # Turn the camera's LED off
    camera.led = False
    camera.start_preview()
    time.sleep(2)
    camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
image = Image.open(stream)