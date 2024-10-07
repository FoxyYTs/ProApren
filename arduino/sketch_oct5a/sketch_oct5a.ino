#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClientSecureBearSSL.h>

const char* ssid = "DAZA";
const char* pass = "1022002153";

void setup() {
  Serial.begin(115200);
  Serial.println("Iniciando Conexion a la RED")

  WiFi.begin(ssid,pass);
  Serial.println("Conectando... en:"+WiFi.SSID())
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(200);
  }

  WiFiClientSecure *client = new WiFiClientSecure;

  delete client;

}

void loop() {
  // put your main code here, to run repeatedly:

}
