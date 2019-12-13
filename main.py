import serial
import time
from sys import exit
from models import Arduino, Sensor


try:
	arduino = Arduino()
except Exception as e:
	print(e)
	exit()

try:
	ldrs = []
	ldrs.append(Sensor(1, arduino))
	ldrs.append(Sensor(2, arduino))
	
except Exception as e:
	print("Error occured creating sensor")


try:	
	time.sleep(1)
	print(arduino.readBuffer())
	while True:
		req_id = int(input(">>> "))
		if req_id == 0:
			arduino.closeConnection()
			exit()
		for ldr in ldrs:
			if ldr.uid == req_id:
				print(ldr.getReading())		
		
		

	


except KeyboardInterrupt:
	print("Keyboard Interrupt") 

finally:
	arduino.closeConnection()
