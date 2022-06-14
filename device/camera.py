from datetime import datetime
from picamera import PiCamera

class Camera:
    def __init__(self) -> None:
        self.camera = PiCamera()

    def capture(self):
        print("Taking photo...")
        now = datetime.now()
        self.camera.capture(f"./server/pigallery2/images/{now}.jpg")
        print(f"{now}.jpg save success")