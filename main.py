# -*- coding: utf-8 -*-
from weather.weather import Weather
from weather.speech import Speech
from device.button import Button
from device.camera import Camera
import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    weather = Weather('부산시 부산진구 엄광로 176')
    speech = Speech()

    button = Button()
    camera = Camera()

    while True:
        if button.check_push_button():
            speech.speech(weather.get_temperature(), weather.get_humidity())
            camera.capture()