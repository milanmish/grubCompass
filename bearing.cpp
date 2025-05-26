#include <Servo.h>

Servo myServo;
String incomingData = "";

void setup() {
    Serial.begin(9600);
    myServo.attach(5);  // figure out which pin is the servo on
  }

void loop() {
    if (Serial.available()) {
        char c = Serial.read();
        if (c == '\n') {
            Serial.println(incomingData);
            int commaIndex = incomingData.indexOf(',');
            float grubLat = incomingData.substring(0, commaIndex).toFloat();
            float grubLon = incomingData.substring(commaIndex + 1).toFloat();


            // finds the angle between the points

            currentLat = 0; // replace later with actual stuff from gps
            currentLon = 0; // replace

            float deltaLat = grubLat - currentLat;
            float deltaLon = grubLon - currentLon;

            float angle = atan2(deltaLat, deltaLon) * 180 / PI;
            if (angle < 0) {
                angle += 360; // normalize angle to 0-360 degrees
            }

            Serial.print("Moving servo to angle: ");
            Serial.println(angle);

            // Move servo (map to 0-180 range for most hobby servos)
            int servoAngle = constrain(map(angle, 0, 360, 0, 180), 0, 180);
            myServo.write(servoAngle);

            incomingData = "";

        } else {
            incomingData += c;
        }
    }
}