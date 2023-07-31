/*
DESCRIPTION:
This example code will uses: Robo Pico and Raspberry Pi Pico / Pico W
to control the servo on the Robo Pico servo port.

AUTHOR  : Cytron Technologies Sdn Bhd
WEBSITE  : www.cytron.io
EMAIL    : support@cytron.io
*/
#include <Servo.h>

Servo myservo1;  // create servo object to control a servo
Servo myservo2;
Servo myservo3;
Servo myservo4;

void setup() {
  myservo1.attach(12);  // attaches the servo on pins to the servo objects
  myservo2.attach(13);
  myservo3.attach(14);
  myservo4.attach(15);
}

void loop() {
  for (int pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    myservo2.write(pos);
    myservo3.write(pos);
    myservo4.write(pos);
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (int pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    myservo2.write(pos);
    myservo3.write(pos);
    myservo4.write(pos);
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
