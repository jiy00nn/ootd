# -*- coding: utf-8 -*-
from weather.weather import Weather
from device.button import Button

if __name__ == '__main__':
    weather = Weather('부산시 부산진구 엄광로 176')
    print(weather.get_temperature())
    print(weather.get_humidity())

    button = Button()
    print(button.check_push_button())