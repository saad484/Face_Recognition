#include <cvzone.h>
#include <Servo.h>

Servo servo;

SerialData serialData(1, 1); //(numOfValsRec,digitsPerValRec)
int valsRec[1];

void setup() {
  serialData.begin();
  pinMode(4, OUTPUT);

  servo.attach(9); // Attach the servo to pin 9
  servo.write(0); // Initialize the servo position to 0 degrees
}

void loop() {
  serialData.Get(valsRec);
  int value = valsRec[0];

  if (value == 1) {
    digitalWrite(4, HIGH); // Turn on the LED
    servo.write(90); // Move the servo to 90 degrees
  } else {
    digitalWrite(4, LOW); // Turn off the LED
    servo.write(0); // Move the servo to 0 degrees
  }

  delay(10);
}
