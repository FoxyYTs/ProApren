#include <ESP8266WiFi.h>

String ssid     = "TP-LINK_0C96";
String password = "labintegrado101";

byte cont = 0;
byte max_intentos = 50;

void setup() {
  //Inicia Serial
  Serial.begin(115200);
  Serial.print("\n");

  Wifi.begin(ssid, password);

  if (cont < max_intentos){
      Serial.println("****");
      Serial.print("WiFi.SS");
      Serialprint("IP: ")

  }
}