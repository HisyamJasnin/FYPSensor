# libraries
import RPi.GPIO as GPIO
import time
from time import strftime
from time import sleep
import mysql.connector
import datetime

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
TRIG = 7
ECHO = 12

# set GPIO direction (IN / OUT)
print("Distance measurement in progress")
GPIO.setup(TRIG, GPIO.OUT)  # declare trigger pin as output
GPIO.setup(ECHO, GPIO.IN)   # declare echo pin as input
dist_from_base = 10.7 # distance from the sensor to the base of the container

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

def main_water():
    while True:
        # for looping 3 times then stop
        dist = distance()
        print("\nDistance: %.1f cm " % dist)
            
        # get percentage of water filled
        percent = (dist_from_base - dist) / dist_from_base  * 100
            
        if dist >= dist_from_base:
            percent = 0
        elif dist <= 2.5:
            percent = 100
        else:
            percent = round(percent)
            
        print("Percentage of water filled: " + str(percent) + " %")
        time.sleep(1)
        break
        
    try:
        # create connection for MySQL
        db = mysql.connector.connect(host= "128.199.176.62",
                                     user= "sam",
                                     password= "password",
                                     port= "3306",
                                     database= "sprinkler")
            
        # create time format for the sensor data
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
            
        # create cursor object
        cursor = db.cursor()
        # get id and username from database
        cursor.execute("""  SELECT Username FROM water_level ORDER BY ID DESC LIMIT 1 """)
        record = cursor.fetchone()
                
        # selecting column value into variable
        username = (record[0])
                
        # Excute SQL command and insert data into database
        cursor.execute(""" UPDATE water_level SET datetime = %s, distance = %s, percentage = %s WHERE Username = %s""",(date,round(dist,1),percent,username))
                
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
                           
