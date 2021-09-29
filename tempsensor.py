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

# function to read raw sensor output file
def raw_temp():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = raw_temp()
    while lines[0].strip()[-3:] != 'YES':
        sleep(0.2)
        lines = raw_temp()

#  to find the line number for the codes and search t= among the line
    temp_result = lines[1].find('t=')

    if temp_result != -1:
        # to cut all the code and leave the temperature value
        temp_string = lines[1].strip()[temp_result + 2:]
        # Temperature in Celcius and to give point on the value
        temp = float(temp_string) / 1000.0
        return temp

# create loop to print out the data every 2 seconds
while True:
    print("Current temperature = " + read_temp() + " °C")
    time.sleep(2)
