#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

SoftwareSerial mySerial(11, 10);  // RX, TX

Adafruit_GPS GPS(&mySerial);

unsigned long previousMillis = 0;  // Time tracker for updates
const unsigned long updateInterval = 2000;  // 500ms = 2Hz

void setup() {
  Serial.begin(115200);      // For debugging
  mySerial.begin(9600);      // GPS default baud (for PA1010D)

  GPS.begin(9600);           // Initialize GPS
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);  // Set which NMEA sentences to output
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_2HZ);     // Set GPS update rate to 2Hz
  GPS.sendCommand(PMTK_API_SET_FIX_CTL_1HZ);     // (Optional) Fix control rate

  Serial.println("Adafruit GPS test!");
}

void loop() {
  char c = GPS.read();
  if (c) {
    Serial.print(c);
  }

  // Update GPS data when new NMEA sentence is received
  if (GPS.newNMEAreceived()) {
    if (!GPS.parse(GPS.lastNMEA())) {
      return;  // Parse NMEA sentence
    }
  }

  // Print GPS data at 500ms intervals (2Hz)
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= updateInterval) {
    previousMillis = currentMillis;

    if (GPS.fix) {
      Serial.print("Latitude: "); Serial.println(GPS.latitude, 4);
      Serial.print("Longitude: "); Serial.println(GPS.longitude, 4);
      Serial.print("Speed (knots): "); Serial.println(GPS.speed);
      Serial.print("Angle: "); Serial.println(GPS.angle);
      Serial.print("Altitude: "); Serial.println(GPS.altitude);
      Serial.print("Satellites: "); Serial.println((int)GPS.satellites);
      Serial.println();
    }
  }
}
