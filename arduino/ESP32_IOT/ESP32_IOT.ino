//Include libraries
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClientSecureBearSSL.h>


//Add WIFI data
const char* ssid = "DAZA";              //Add your WIFI network name 
const char* password =  "1022002153";           //Add WIFI password


//Variables used in the code
String LED_id = "1";                  //Just in case you control more than 1 LED
bool toggle_pressed = false;          //Each time we press the push button    
String data_to_send = "";             //Text data to send to the server
unsigned int Actual_Millis, Previous_Millis;
int refresh_time = 200;               //Refresh rate of connection to website (recommended more than 1s)


//Inputs/outputs                   //Connect push button on this pin
int LED = 16;                          //Connect LED on this pin (add 150ohm resistor)


//Button press interruption
void IRAM_ATTR isr() {
  toggle_pressed = true; 
}

void setup() {
  delay(10);
  Serial.begin(115200);                   //Start monitor
  pinMode(LED, OUTPUT);                   //Set pin 2 as OUTPUT

  WiFi.begin(ssid, password);             //Start wifi connection
  Serial.print("Connecting...");
  while (WiFi.status() != WL_CONNECTED) { //Check for the connection
    delay(500);
    Serial.print(".");
  }
  if(WiFi.status() == WL_CONNECTED){
    Serial.println("\n********************************************");
    Serial.println("Conectado a la red WiFi: ");
    Serial.println(WiFi.SSID());
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
    Serial.print("macAdress: ");
    Serial.println(WiFi.macAddress());
    Serial.println("*********************************************");
  }

  Serial.print("Connected, my IP: ");
  Serial.println(WiFi.localIP());
  Actual_Millis = millis();               //Save time for refresh loop
  Previous_Millis = Actual_Millis; 
}


void loop() {  
  //We make the refresh loop using millis() so we don't have to sue delay();
  Actual_Millis = millis();
  if(Actual_Millis - Previous_Millis > refresh_time){
    Previous_Millis = Actual_Millis;  
    if(WiFi.status()== WL_CONNECTED){                   //Check WiFi connection status  
      std::unique_ptr<BearSSL::WiFiClientSecure>client(new BearSSL::WiFiClientSecure);

    // Ignore SSL certificate validation
      client->setInsecure();
    
    //create an HTTPClient instance
      HTTPClient https;                               //Create new client
      if(toggle_pressed){                               //If button was pressed we send text: "toggle_LED"
        data_to_send = "toggle_LED=" + LED_id;  
        toggle_pressed = false;                         //Also equal this variable back to false 
      }
      else{
        data_to_send = "check_LED_status=" + LED_id;    //If button wasn't pressed we send text: "check_LED_status"
      }
      
      //Begin new connection to website       
      Serial.print("[HTTPS] begin...\n");
      if (https.begin(*client, "https://foxyyts.github.io/ArqHard/esp32_update.php")) {         //Prepare the header
        Serial.print("[HTTPS] GET...\n");
        int response_code = https.POST(data_to_send);                                //Send the POST. This will giveg us a response code
      
      //If the code is higher than 0, it means we received a response
        if(response_code > 0){
          Serial.println("HTTP code " + String(response_code));                     //Print return code
    
          if(response_code == 405){                                                 //If code is 200, we received a good response and we can read the echo data
            String response_body = https.getString();                                //Save the data comming from the website
            Serial.print("Server reply: ");                                         //Print data to the monitor for debug
            Serial.println(response_body);

            //If the received data is LED_is_off, we set LOW the LED pin
            if(response_body == "LED_is_off"){
              digitalWrite(LED, LOW);
            }
            //If the received data is LED_is_on, we set HIGH the LED pin
            else if(response_body == "LED_is_on"){
              digitalWrite(LED, HIGH);
            }  
          }//End of response_code = 200
        }//END of response_code > 0
        
        else{
        Serial.print("Error sending POST, code: ");
        Serial.println(response_code);
        }
        https.end();
      }                                                                 //End the connection
    }//END of WIFI connected
    else{
      Serial.println("WIFI connection error");
    }
  }
}
