# import libraries
#!/usr/bin/env python
import os
import time
from time import sleep
from time import strftime
import datetime
import mysql.connector

# Load drivers
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# define the location for the sensor output is located
temp_sensor = '/sys/bus/w1/devices/28-3c01f095948b/w1_slave'

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
     print("Current temperature = " + str(read_temp()) + " °C")
     time.sleep(2)
     break
     
try:
    # create connection for MySQL
    db = mysql.connector.connect(host= "128.199.176.62",
                                 user= "sam",
                                 password= "password",
                                 port= "3306",
                                 database= "sensor_database")
    
    # create time format for the sensor data
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d %H:%M:%S')
         
    # create cursor object
    cursor = db.cursor()
    # Excute SQL command and insert data into database
    cursor.execute(""" INSERT INTO tempLog (datetime,temperature) VALUES (%s,%s) """,(date,read_temp()))
    # Commit changes in the database
    db.commit()

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))
     
finally:
    # close cursor and end connection to database
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection is closed")

    

