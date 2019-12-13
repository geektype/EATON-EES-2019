String serial_string = "";


int sensors[2] = {A5,A4};


void setup() {
  // Start Serial Connection
  Serial.begin(9600);

  Serial.print("Arduino Ready to recieve");

  //Initialise all if the pins as input
  for (int i = 0; i < sizeof(sensors); i++)
  {
    pinMode(sensors[i], INPUT);
  }
  
}

void loop() {
  //If serial is not available then do nothing
  while (!Serial.available()) {}
  while (Serial.available()){
    
    if (Serial.available() > 0){
      //Read the buffer until you reach \n
      serial_string = Serial.readStringUntil('\n');
    }
  }
  
  if (serial_string.length() >0)
  {
    //What to do with different ids given
    switch (serial_string.toInt())
    {
    case 1:
      Serial.print(analogRead(sensors[0]));
    break;

    case 2:
      Serial.print(analogRead(sensors[1]));
    break;
    

    default:
      Serial.print("Invalid device ID."); // if no match is found
    }

  }
}
