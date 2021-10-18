# libraries
import RPi.GPIO as GPIO
import time
import mysql.connector
from time import strftime
from time import sleep
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
    try:
        while True:
            dist = distance()
            print("Distance: %.1f cm " % dist)
            time.sleep(1)
            
            print("clean up")
            GPIO.cleanup() # cleanup all GPIO
            break
            
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
        # get username from database
        cursor.execute(""" SELECT Username FROM water_level ORDER BY ID DESC LIMIT 1 """)
        record = cursor.fetchone()
            
        # selecting column value into variable
        username = (record[0])
            
        # Excute SQL command and insert data into database
        cursor.execute(""" UPDATE water_level SET datetime = %s, distance =%s WHERE Username = %s""",(date,str(round(dist,1)),username))
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

        
                                                                         
