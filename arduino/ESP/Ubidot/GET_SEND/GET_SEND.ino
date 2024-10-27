/****************************************
 * Include Libraries
 ****************************************/
#include "UbidotsESPMQTT.h"

/****************************************
 * Define Constants
 ****************************************/
#define TOKEN "BBUS-bXgmuWeuji822RqGKmFwSHXva4h8hO" // Your Ubidots TOKEN
#define WIFINAME "DAZA" //Your SSID
#define WIFIPASS "1022002153" // Your Wifi Pass
#define DEVICE_LABEL  "elaparato"  // Put here your Ubidots device label
#define D0 16

Ubidots client(TOKEN);

/****************************************
 * Auxiliar Functions
 ****************************************/

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println((char)payload[0]);
  if((char)payload[0] == '1'){
    digitalWrite(D0, HIGH);
  }else{
    digitalWrite(D0, LOW);
  }
}

/****************************************
 * Main Functions
 ****************************************/

void setup() {
  pinMode(D0, OUTPUT);
  Serial.begin(115200);
  client.wifiConnection(WIFINAME, WIFIPASS);
  client.begin(callback);
  client.ubidotsSubscribe(DEVICE_LABEL, "led");
  }

void loop() {
  // put your main code here, to run repeatedly:
  if(!client.connected()){
    client.reconnect();
    client.ubidotsSubscribe(DEVICE_LABEL, "led");
    Serial.print("Que chulo");
  }
  
  float value1 = analogRead(0);
  //float value2 = analogRead(2)
  client.add("temperature", value1);
  //client.add("status", value2);
  client.ubidotsPublish("elaparato");
  client.loop();
}