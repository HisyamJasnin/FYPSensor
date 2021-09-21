# import libraries for sensor
import time
from w1thermsensor import W1ThermSensor

# store connection
sensor = W1ThermSensor()

# to get the temperature sensor data every second
while True:
    temperature = sensor.get_temperature()

    # format temperature data to be printed from an float to a string
    print("The temperature is %s celsius" % temperature)

    # wait for 1 second between taking temperature reading
    time.sleep(1)
