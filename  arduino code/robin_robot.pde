/*
 * ------------------------------
 *   MultipleSerialServoControl
 * ------------------------------
 *
 * Uses the Arduino Serial library
 *  (http://arduino.cc/en/Reference/Serial)
 * and the Arduino Servo library
 *  (http://arduino.cc/en/Reference/Servo)
 * to control multiple servos from a PC using a USB cable.
 *
 * Dependencies:
 *   Arduino 0017 or higher
 *     (http://www.arduino.cc/en/Main/Software)
 *   Python servo.py module
 *     (http://principialabs.com/arduino-python-4-axis-servo-control/)
 *
 * Created:  23 December 2009
 * Author:   Brian D. Wendt
 *   (http://principialabs.com/)
 * Version:  1.0
 * License:  GPLv3
 *   (http://www.fsf.org/licensing/)
 *
 */

// Import the Arduino Servo library
#include <Servo.h> 

// Create a Servo object for each servo
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;
Servo servo9;
// TO ADD SERVOS:
//   Servo servo5;
//   etc...

// Common servo setup values
int minPulse = 600;   // minimum servo position, us (microseconds)
int maxPulse = 2400;  // maximum servo position, us

// User input for servo and position
int userInput[3];    // raw input from serial buffer, 3 bytes
int startbyte;       // start byte, begin reading input
int servo;           // which servo to pulse?
int pos;             // servo angle 0-180
int i;               // iterator

void setup() 
{ 
  
  pinMode(19,OUTPUT);
  pinMode(18,OUTPUT);
  pinMode(17,OUTPUT);
	
// Attach each Servo object to a digital pin
  servo1.attach(8, minPulse, maxPulse);
  servo2.attach(7, minPulse, maxPulse);
  servo3.attach(6, minPulse, maxPulse);
  servo4.attach(5,minPulse, maxPulse);
  servo5.attach(9,minPulse,maxPulse);
  servo6.attach(10,minPulse,maxPulse);
  servo7.attach(4,minPulse,maxPulse);
  servo8.attach(3,minPulse,maxPulse);
   


// TO ADD SERVOS:
  //   servo5.attach(YOUR_PIN, minPulse, maxPulse);
  //   etc...

  // Open the serial connection, 9600 baud
  Serial.begin(9600);
  
} 

void loop() 
{ 
  

// Wait for serial input (min 3 bytes in buffer)
  if (Serial.available() > 2) {
    // Read the first byte
    startbyte = Serial.read();
    // If it's really the startbyte (255) ...
    if (startbyte == 255) {
      // ... then get the next two bytes
      for (i=0;i<2;i++) {
        userInput[i] = Serial.read();
      }
      // First byte = servo to move?
      servo = userInput[0];
      // Second byte = which position?
      pos = userInput[1];
      // Packet error checking and recovery
      if (pos == 255) { servo = 255; }

      // Assign new position to appropriate servo
      switch (servo) {
        case 1:
          servo1.write(pos);    // move servo1 to 'pos'
          break;
        case 2:
          servo2.write(pos);
          break;
        case 3:
          servo3.write(pos);
          break;
        case 4:
          servo4.write(pos);
          break;
	case 5:
          servo5.write(pos);
          break;
	case 6:
          servo6.write(pos);
          break;
	case 7:
          servo7.write(pos);
          break;
	case 8:
          servo8.write(pos);
          break;
	case 9:
          servo9.write(pos);
          break;
                  
	case 10:
	  
	   digitalWrite(19, HIGH);
	   delay(100);
	   digitalWrite(19, LOW);
	   delay(100);   
  	   break;
	
	case 11:
	  digitalWrite(18, HIGH);
	   delay(100);
	   digitalWrite(18, LOW);
	   delay(100);   
  	   break;   	
	case 12:
	   digitalWrite(17, HIGH);
	   delay(100);
	   digitalWrite(17, LOW);
	   delay(100);      
  	   break;
      }
    }
  }


}
