import mysql.connector
from models import Sensor, Arduino, storeReadings
from cred import *
import time



arduino = Arduino()

ldrs = [] #This array stores all of the sensors
ldrs.append(Sensor(1, arduino, "sensor1"))
ldrs.append(Sensor(2, arduino, "sensor2"))
ldrs.append(Sensor(3, arduino, "sensor3"))
ldrs.append(Sensor(4, arduino, "sensor4"))


time.sleep(0.75)
arduino.readBuffer()

readings = []
for sensor in ldrs:
    print("reading")
    readings.append([str(sensor.name) ,sensor.getReading()])

print(readings)


storeReadings(readings)

arduino.closeConnection()