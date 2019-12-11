import serial
import time
from sys import exit

serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

def getReading(sensor_id):
	try:
		sensor_id += "\n"
		b = sensor_id.encode('ASCII')
		serialPort.write(b)

		time.sleep(1)
		if(serialPort.in_waiting > 0):
			while serialPort.in_waiting > 0:
				serialString = serialPort.readline()
				# print(serialString)
				return serialString.decode('ASCII')
	except Exception as e:
		return e

def readBuffer():
	time.sleep(2)
	if(serialPort.in_waiting > 0):
		while serialPort.in_waiting > 0:
			serialString = serialPort.readline()
			# print(serialString)
			print(serialString.decode('ASCII'))
try:
	readBuffer()
	
	while True:
		

		sensor_id = input(">>> ")
		if sensor_id == "q" or sensor_id=="exit":
			print("Exiting. Goodbye!")
			serialPort.close()
			exit()
		elif sensor_id != "":
			print(getReading(sensor_id))

	


except KeyboardInterrupt:
	print("Keyboard Interrupt") 

finally:
	serialPort.close()
