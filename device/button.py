import RPi.GPIO as GPIO
import time

class Button:
    def __init__(self) -> None:
        GPIO.setup(24, GPIO.IN)

    def check_push_button(self) -> bool:
        while True:
            value = GPIO.input(24)
            if not value:
                time.sleep(0.5)
                break
        return True