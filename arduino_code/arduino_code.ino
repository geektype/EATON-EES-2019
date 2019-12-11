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
    Serial.print("Readings on sensor id: ");  
    Serial.print(serial_string);
    if (serial_string.toInt() == 1){
      digitalWrite(13, HIGH);
    } else if(serial_string.toInt() == 10) {
      digitalWrite(13, LOW);
    }
  } 
}
