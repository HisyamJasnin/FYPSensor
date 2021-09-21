# libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
TRIG = 21
ECHO = 20

# set GPIO direction (IN / OUT)
while True:
    print("Distance measurement in progress")
    GPIO.setup(TRIG, GPIO.OUT)  # declare trigger pin as output
    GPIO.setup(ECHO, GPIO.IN)   # declare echo pin as input

    GPIO.output(TRIG, False)    # make the trigger pin to be low - to stabilize the sensor
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001) # wait 10 micro second
    GPIO.otuput(TRIG, False)

    # save start time
    while GPIO.input(ECHO) == 0:    # wait till echo is low
        pulse_start = time.time()

    # save time of arrival
    while GPIO.input(ECHO) == 1:    # wait here till echo is high
        pulse_end = time.time()

        # time difference between start and end
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Distance: ", distance, " cm")
        time.sleep(2)

    # Reset by pressing CTRL + C
        except KeyboardInterrupt:
        print("Measurement stopped by the User")
        GPIO.cleanup()
