import serial
import time

class Arduino:
    """ 
        Class to model a serail connection to an arduino.
    """


    def __init__(self):
        #Initialise Connection
        #Change /dev/ttyACM0 to serial port arduino is connected to.
        self.serial_connection = serial.Serial(port = "/dev/ttyACM0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
    
    def readBuffer(self):
        """
            Reads all the content stored in the serial buffer and returns content as a string
        """
        time.sleep(1) #Delay to make sure every thing has been transfered.
        #Only do if the buffer is not empty
        if(self.serial_connection.in_waiting > 0):
            #Keep repeating until buffer is not empty so it can read all of the message.
            while self.serial_connection.in_waiting > 0:
                serialString = self.serial_connection.readline()
                return serialString.decode('ASCII') #Return the line formatted in ASCII
    
    def sendData(self, data):
        """
            Sends given data over the serial connection encodded in byte form encodded as ASCII
        """
        try:
            #Adds newline so the arduino knows when to stop listening
            self.send_data = str(data) + "\n"
            #Convert to ASCII byte form
            self.send_data_b = self.send_data.encode('ASCII')
            self.serial_connection.write(self.send_data_b)
            return True
        except Exception:
            return False

    def closeConnection(self):
        """
            Closes current serial connection and frees up the device and COM port.
        """
        self.serial_connection.close()

class Sensor:
    """
        Class to model a single sensors. 
        uid : unique identifier for the sensor - must match the record on the arduino too
        last_reading : The last fetched reading
        host : The device which the sensor is connected to Also the serial connection over which to communicate on.
               use class Arduino()
    """

    def __init__(self, uid, host):
        self.uid = uid
        
        self.last_reading = None
        self.host = host
    

    def getReading(self):
        self.host.sendData(self.uid)
        self.reading = self.host.readBuffer()
        self.last_reading = self.reading
        return self.reading

