int ps;
void setup() {
  pinMode (9, OUTPUT);
  pinMode (10, OUTPUT);
  pinMode (11, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  ps = random(20,45);
  Serial.println(ps);
  delay(1000);

  char lecturaSerial = Serial.read();
  if (lecturaSerial == 'H'){
    digitalWrite (9, HIGH);
    digitalWrite (10, LOW);
    digitalWrite (11, LOW);
  }
    if (lecturaSerial == 'N'){
    digitalWrite (11, HIGH);
    digitalWrite (9, LOW);
    digitalWrite (10, LOW);
  }
    if (lecturaSerial == 'F'){
    digitalWrite (10, HIGH);
    digitalWrite (9, LOW);
    digitalWrite (11, LOW);
  }
}
