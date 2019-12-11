String serial_string = "";
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  Serial.print("Arduino Ready to recieve");

  pinMode(13, OUTPUT);
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
    if (serial_string.toInt() == 1){
      Serial.print(analogRead(A5));
    }

  
  } 
}
