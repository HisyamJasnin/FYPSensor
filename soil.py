# import libraries
import Rpi.GPIO as GPIO
import time

# Setup GPIO
soil = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil, GPIO.IN)

def callback(soil):
    if GPIO.input(soil):
        print("Water Detected!")
    else:
        print("No Water Detected!")

# to know whether the pin goes HIGH or LOW
GPIO.add_event_detect(soil, GPIO.BOTH, bouncetime=300)

# give function to GPIO pin to run when there is changes
GPIO.add_event_callback(input, callback)

# initialize loop
while True:
    time.sleep(1)