String serial_string = "";


int sensors[2] = {A5,A4};


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  Serial.print("Arduino Ready to recieve");

  for (int i = 0; i < sizeof(sensors); i++)
  {
    pinMode(sensors[i], INPUT);
  }
  
}

void loop() {
  while (!Serial.available()) {}

  while (Serial.available()){
    
    if (Serial.available() > 0){
      serial_string = Serial.readStringUntil('\n');
    }
  }
  
  if (serial_string.length() >0)
  {
    switch (serial_string.toInt())
    {
    case 1:
      Serial.print(analogRead(sensors[0]));
    break;

    case 2:
      Serial.print(analogRead(sensors[1]));
    break;
    

    default:
      Serial.print("Invalid device ID.");
    }

  }
}
