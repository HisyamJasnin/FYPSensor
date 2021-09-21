# !/usr/bin/python
# import libraries
import RPi.GPIO as GPIO
import time

pin_rain= 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_rain, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
try :
while True:
    status = GPIO.input(pin_rain)
    if status == True:
        print("No raindrops were detected, it is not raining")
    else:
        print("Raindrops detected, it is raining")
        time.sleep(0.5)
