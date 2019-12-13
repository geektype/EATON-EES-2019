import serial
import time
from sys import exit
from models import Arduino, Sensor #Import models from models.py


try:
	arduino = Arduino()
except Exception as e:
	#Print the erro if it occurs
	print(e)
	exit()

try:
	ldrs = [] #This array stores all of the sensors
	ldrs.append(Sensor(1, arduino))
	ldrs.append(Sensor(2, arduino))
	
except Exception as e:
	print("Error occured creating sensor")


try:	
	#Wait for the arduino to return startup message
	time.sleep(1)
	print(arduino.readBuffer())
	while True:
		req_id = int(input(">>> "))
		if req_id == 0:
			arduino.closeConnection()
			exit()
		#Look if uid exists
		for ldr in ldrs:
			if ldr.uid == req_id:
				#If it exists then print the current reading
				print(ldr.getReading())		
		
		

	


except KeyboardInterrupt:
	print("Keyboard Interrupt") 

finally:
	arduino.closeConnection()

