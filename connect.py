# To test connection on MySQL databases and extract one record from table
# import libraries
import mysql.connector

try:
    db = mysql.connector.connect(host="128.199.176.62",
                                 user="sam",
                                 password="password",
                                 port="3306",
                                 database="sensor_database")
    
    sql_Query = " SELECT temperature FROM tempLog WHERE id = %s"
    id = (1,)
    cursor = db.cursor()
    cursor.execute(sql_Query, id)
    record = cursor.fetchone()
    
    # selecting column value into variable
    temp = float(record[0])
    print("Current temperature: ", temp)
    
except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))
    
finally:
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection is closed")
