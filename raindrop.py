# !/usr/bin/python
# import libraries
from time import sleep
import os
import RPi.GPIO as GPIO

pin_rain= 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_rain, GPIO.IN)

try :
while True:
    status = GPIO.input(pin_rain)
    if status == True:
        print("No raindrops were detected, it is not raining")
    else:
        print("Raindrops detected, it is raining")
        time.sleep(0.5)
