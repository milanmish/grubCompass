String incomingData = "";

void setup() {
    Serial.begin(9600);
  }

void loop() {
    if (Serial.available()) {
        char c = Serial.read();
        if (c == '\n') {
            Serial.println(incomingData);
            int commaIndex = incomingData.indexOf(',');
            float grubLat = incomingData.substring(0, commaIndex).toFloat();
            float grubLon = incomingData.substring(commaIndex + 1).toFloat();
            
        } else {
            incomingData += c;
        }
    }
}