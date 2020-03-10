from models import Sensor, Arduino, storeReadings
from cred import *
import time
import json
import boto3


def toTemp(current):
    return ((400/61)*float(current)) - (1636/61)

client = boto3.client('kinesis')
arduino = Arduino()

ldrs = [] #This array stores all of the sensors
ldrs.append(Sensor(1, arduino, "sensor1"))
ldrs.append(Sensor(2, arduino, "sensor2"))
ldrs.append(Sensor(3, arduino, "sensor3"))
ldrs.append(Sensor(4, arduino, "sensor4"))

sensor = Sensor(1, arduino, "test")

time.sleep(2)
try:
    while True:
        readings = sensor.getReading()
        reading_dict = json.dumps({'sensor1':toTemp(readings[0]), 'sensor2':toTemp(readings[1]), 'sensor3':toTemp(readings[2]), 'sensor4':toTemp(readings[3])})
        response = client.put_record(StreamName="testStream", Data=reading_dict, PartitionKey="partitionkey")
        print(reading_dict)
except KeyboardInterrupt:
    print("exiting")
    arduino.closeConnection()