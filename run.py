import mysql.connector
from models import Sensor, Arduino, create_connection, storeReadings
from cred import *
import time

db_conn, cursor = create_connection(HOST, USERNAME, PASSWORD, DATABASE)

arduino = Arduino()

ldrs = [] #This array stores all of the sensors
ldrs.append(Sensor(1, arduino, "ldr1"))
ldrs.append(Sensor(2, arduino, "ldr2"))


time.sleep(0.75)
arduino.readBuffer()

readings = []
for sensor in ldrs:
    print("reading")
    readings.append([str(sensor.name) ,sensor.getReading()])

print(readings)


storeReadings(readings, cursor)

db_conn.commit()
arduino.closeConnection()