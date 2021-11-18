# import libraries
import RPi.GPIO as GPIO
import time

# Setup GPIO
soil = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil, GPIO.IN)

def callback(soil):
    if GPIO.input(soil):
        print("No Water Detected!")
    else:
        print("Water Detected!")
        
# to know whether the pin goes HIGH or LOW
GPIO.add_event_detect(soil, GPIO.BOTH, bouncetime=300)

# give function to GPIO pin to run when there is changes
GPIO.add_event_callback(soil, callback)

# initialize loop
while True:
    callback(soil)
    time.sleep(1)
