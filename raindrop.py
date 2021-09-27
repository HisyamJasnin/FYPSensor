# !/usr/bin/python
# import libraries
import time
import os
import RPi.GPIO as GPIO

# set GPIO pins
pin_rain = 22

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO direction 
GPIO.setup(pin_rain, GPIO.IN) #declare it as input

try:
    while True:
        status = GPIO.input(pin_rain)
        if status == 0: # if there is a water present on the board 
            print("Raindrops detected, it is raining")
            time.sleep(1.0)
        else:
            print("No Raindrops detected, it is not raining")
            time.sleep(1.0)
    
# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Raindrop detection stopped by the user")
    
finally:
    print("clean up the GPIO")
    GPIO.cleanup() # cleanup all GPIO
            
            

