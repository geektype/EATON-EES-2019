import serial
import time

class Arduino:
    
    def __init__(self):
        self.serial_connection = serial.Serial(port = "/dev/ttyACM0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    
    def readBuffer(self):
        time.sleep(2)
        if(self.serial_connection.in_waiting > 0):
            while self.serial_connection.in_waiting > 0:
                serialString = self.serial_connection.readline()
                # print(serialString)
                return serialString.decode('ASCII')
    
    def sendData(self, data):
        try:
            self.send_data = str(data) + "\n"
            self.send_data_b = self.send_data.encode('ASCII')
            self.serial_connection.write(self.send_data_b)
            return True
        except Exception:
            return False

    def closeConnection(self):
        self.serial_connection.close()

class Sensor:

    def __init__(self, uid, host):
        self.uid = uid
        self.last_reading = None
        self.host = host
    

    def getReading(self):
        self.host.sendData(self.uid)
        self.reading = self.host.readBuffer()
        self.last_reading = self.reading
        return self.reading

