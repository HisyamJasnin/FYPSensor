# import libraries
import RPi.GPIO as GPIO
import time

# GPIO setmode(BOARD/BCM(BroadCoM))
GPIO.setmode(GPIO.BCM)

# Initialize the GPIO pins for the relay
relay_1 = 23
relay_2 = 24
relay_3 = 20
relay_4 = 21

# Relay 1
GPIO.setup(relay_1, GPIO.OUT)
# Relay 2
GPIO.setup(relay_2, GPIO.OUT)
# Relay 3
GPIO.setup(relay_3, GPIO.OUT)
# Relay 4
GPIO.setup(relay_4, GPIO.OUT)

# create loop to test the relay
try:
    while True:
        # to turn on relay
        GPIO.output(relay_1, GPIO.HIGH)
        print("Relay 1 ON")
        time.sleep(1)

        GPIO.output(relay_2, GPIO.HIGH)
        print("Relay 2 ON")
        time.sleep(1)

        GPIO.output(relay_3, GPIO.HIGH)
        print("Relay 3 ON")
        time.sleep(1)

        GPIO.output(relay_4, GPIO.HIGH)
        print("Relay 4 ON")
        time.sleep(1)

        # to turn off relay
        GPIO.output(relay_1, GPIO.LOW)
        print("Relay 1 OFF")
        time.sleep(1)

        GPIO.output(relay_2, GPIO.LOW)
        print("Relay 2 OFF")
        time.sleep(1)

        GPIO.output(relay_3, GPIO.LOW)
        print("Relay 3 OFF")
        time.sleep(1)

        GPIO.output(relay_4, GPIO.LOW)
        print("Relay 4 OFF")
        time.sleep(1)

# Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Test for relay is stopped by the user")

finally:
        # clean up the GPIO pins
        GPIO.cleanup()
