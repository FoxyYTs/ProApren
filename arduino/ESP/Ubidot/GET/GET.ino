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
#define VARIABLE_LABEL  "led"  // Put here your Ubidots variable label 
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
  // put your setup code here, to run once:
  //client.ubidotsSetBroker("industrial.api.ubidots.com"); // Sets the broker properly for the business account
  //client.setDebug(false); // Pass a true or false bool value to activate debug messages
  Serial.begin(115200);
  client.wifiConnection(WIFINAME, WIFIPASS);
  client.begin(callback);
  client.ubidotsSubscribe(DEVICE_LABEL, VARIABLE_LABEL); //Insert the dataSource and Variable's Labels
  }

void loop() {
  // put your main code here, to run repeatedly:
  if(!client.connected()){
    client.reconnect();
    client.ubidotsSubscribe(DEVICE_LABEL, VARIABLE_LABEL);
  }
  
  client.loop();
  }