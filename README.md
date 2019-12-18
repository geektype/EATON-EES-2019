[![Documentation Status](https://readthedocs.org/projects/ees-project/badge/?version=latest)](https://ees-project.readthedocs.io/en/latest/?badge=latest)

# EES Project 


## v.0.01 
A communication interface between an Arduino and a host machine over a serial connection. 

## Features

 - Establishes communication over  serial interface
 - Able to send and receive data encoded in ASCII format
 - Arduino can handle up to 6 LDRs and can return their reading
 - Each sensor is identified using a unique identifier to send and receive data
 - Program contains database of sensors and can handle incorrect UIDs
 
 ## Usage
 Import the file containing the models
 ```python 
 from models import Arduino, Sensor
 ```

Create an instance of a serial connection to the Arduino
```python 
arduino = Arduino()
```
This creates an object with the following attributes:
|attr|  value|
|--|--|
|port|`/dev/ttyACM0` |
|baudrate|`9600`|
|bytesize|`8`|
|timeout |`2`|
|stopbits | `serial.STOPBITS_ONE`|

If any of the attributes need to be changed change the instable variable. Eg. to change the port:
```python
arduino.port = "/dev/ttyACM0"
```


Create and add to the array storing all of the sensors
```python 
ldrs = [] 
```

To initialise a sensor:

`main.py`
```python
ldr = Sensor(1, arduino)
```
`1` is the unique id given to this sensor. This will be used to identify the sensor. This **must** be a unique id.

`arduino` is the `Arduino()` object created earlier. This tells the program where to communicate about the sensor.



Say for example the sensor is attached to pin A5.

`arduino_code.ino`

```c++
int sensors[2] = {A4,A5}; # add A5 to the array

...

switch (serial_string.toInt())
    {
    case 1:
      Serial.print(analogRead(sensors[0]));
    break;
    // Add your own case statement 
    case 2:
      Serial.print(analogRead(sensors[1]));
    break;

...
```

To get a reading from a sensor

```python
print(ldr.getReading())
```

To read what is currently in the serial buffer simply do
```python
arudino.readBuffer()
```
Close the connection:
```python
arduino.closeConnection()
```
