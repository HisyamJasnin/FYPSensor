# import libraries
#!/usr/bin/env python
import os
import time
from time import sleep

# Load drivers
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# define the location for the sensor output is located
temp_sensor = '/sys/bus/w1/devices/Sensor_name/w1_slave'

# function to read sensor output file
def read_temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = read_temp_raw()

    temp_result = lines[1].find('t=')

    if temp_result != -1:
        temp_string = lines[1].strip()[temp_result + 2:]
        # Temperature in Celcius
        temp = float(temp_string) / 1000.0
        return temp

# create loop to print out the data every 2 seconds
while True:
    print(read_temp())
    time.sleep(2)
