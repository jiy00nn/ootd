from time import time
import RPi.GPIO as GPIO
import time

class Button:
    def __init__(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.IN)

    def check_push_button(self) -> bool:
        value = GPIO.input(24)
        while not value:
            time.sleep(0.5)
            return value
        

    