import serial
import time
from sys import exit
serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialStirng = ""
print("Starting communication")
time.sleep(2)
if(serialPort.in_waiting > 0):
	while serialPort.in_waiting > 0:
		serialString = serialPort.readline()
		# print(serialString)
		print(serialString.decode('ASCII'))
try:
		while True:
			time.sleep(1)
			if(serialPort.in_waiting > 0):
				while serialPort.in_waiting > 0:
					serialString = serialPort.readline()
					# print(serialString)
					print(serialString.decode('ASCII'))

			send_string = input(">>> ")
			if send_string == "q" or send_string=="exit":
				print("Exiting. Goodbye!")
				serialPort.close()
				exit()

			send_string += "\n"
			b = send_string.encode('ASCII')
			serialPort.write(b)

except KeyboardInterrupt:
	print("Keyboard Interrupt") 

finally:
	serialPort.close()
