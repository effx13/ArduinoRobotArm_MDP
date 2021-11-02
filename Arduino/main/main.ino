#include <Servo.h> 

int servoPin = 9;
Servo servo;
int angle = 0;

void setup() {
  Serial.begin(9600);
  servo.attach(servoPin);
}

void loop() {
    while( Serial.available() ==0 ) {}
      int angle = Serial.parseInt();
    servo.write(angle); 
}
