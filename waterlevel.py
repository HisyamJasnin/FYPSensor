# libraries
import RPi.GPIO as GPIO
import time
from time import strftime
from time import sleep

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
TRIG = 7
ECHO = 12

# set GPIO direction (IN / OUT)
print("Distance measurement in progress")
GPIO.setup(TRIG, GPIO.OUT)  # declare trigger pin as output
GPIO.setup(ECHO, GPIO.IN)   # declare echo pin as input
dist_from_base = 11.1 # distance from the sensor to the base of the container

def distance():
    # set Trigger to HIGH
    GPIO.output(TRIG, True)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    StartTime = time.time()
    StopTime = time.time()
    
    # save StartTime
    while GPIO.input(ECHO) ==0:
        StartTime = time.time()
        
    # save time of arrival
    while GPIO.input(ECHO) ==1:
        StopTime = time.time()
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance

if __name__ == '__main__':
    while True:
        dist = distance()
        print("Distance: %.1f cm " % dist)
        # get percentage of water filled
        percent = (dist_from_base - dist) / dist_from_base  * 100
        percent = round(percent)
        print("Water level: " + str(percent) + " %")
        
        time.sleep(1)