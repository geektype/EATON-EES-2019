# EES Project 

## v.0.01 documentation
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


## Models
### Arduino
```python
class Arduino:
    """ 
        Class to model a serail connection to an arduino.
    """


    def __init__(self):
        #Initialise Connection
        ...
```
| attr | value | description
|--|--|--|
| `self.serialConnection` | `serial.Serial(port = "/dev/ttyACM0", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)` | Parameters to intitialise the serial connection |
For more information on the attributes of the serial Module see [Docs](https://pyserial.readthedocs.io/en/latest/shortintro.html)

#### Methods
`self.readBuffer()`
```python
def readBuffer(self):
        """
            Reads all the content stored in the serial buffer and returns content as a string
        """
```
| attr | value  | description
|--|--| --|
|None  | - | -


---
**NOTE**

There is a 1 second delay built-in to ensure the most up to date bufer is read

---
`self.sendData()`
```python
def sendData(self, data):
        """
            Sends given data over the serial connection encodded in byte form encodded as ASCII
        """
```
| attr | value  | description
|--|--| --|
|`self.data`| data | The data to be sent to the device as a string

The string is converted to a byte and encodded in ascii before being sent

Returns `True` if succesful. 
Returns `False` if exception occured

### Sensor
```python
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
```
| attr | value  | description
|--|--| --|
|self.uid| uid | The unique indentifier for the sensor object
|self.last_reading| None | The last fetched reading
|self.host | arduino | The device which the sensor is connected to