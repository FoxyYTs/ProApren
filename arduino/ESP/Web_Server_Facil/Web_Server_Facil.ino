// Creado ChepeCarlos de ALSW
// Tutorial Completo en https://nocheprogramacion.com
// Canal Youtube https://youtube.com/alswnet?sub_confirmation=1


#if defined(ESP32)
//Librerias para ESP32
#include <WiFi.h>
#include <WiFiMulti.h>
WiFiMulti wifiMulti;

#elif defined(ESP8266)
//Librerias para ESP8266
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
ESP8266WiFiMulti wifiMulti;

#endif

#include "data.h"

int pinLed = 2;
int Estado = 10;

const uint32_t TiempoEsperaWifi = 5000;

unsigned long TiempoActual = 0;
unsigned long TiempoAnterior = 0;
const long TiempoCancelacion = 500;

WiFiServer servidor(80);

void setup() {
  Serial.begin(115200);
  Serial.println("\nIniciando multi Wifi");

  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
  apagar();

  wifiMulti.addAP(ssid_1, password_1);
  wifiMulti.addAP(ssid_2, password_2);

  WiFi.mode(WIFI_STA);
  Serial.print("Conectando a Wifi ..");
  while (wifiMulti.run(TiempoEsperaWifi) != WL_CONNECTED) {
    Serial.print(".");
  }
  Serial.println(".. Conectado");
  Serial.print("SSID:");
  Serial.print(WiFi.SSID());
  Serial.print(" ID:");
  Serial.println(WiFi.localIP());

  servidor.begin();

}

void loop() {
  WiFiClient cliente = servidor.available();

  if (cliente) {
    Serial.println("Nuevo Cliente");
    TiempoActual = millis();
    TiempoAnterior = TiempoActual;
    String LineaActual = "";

    while (cliente.connected() && TiempoActual - TiempoAnterior <= TiempoCancelacion) {
      if (cliente.available()) {
        TiempoActual = millis();
        char Letra = cliente.read();
        if (Letra == '\n') {
          if (LineaActual.length() == 0) {
            if (Estado==0){
              apagar();
              numero0();
            } else if (Estado==1){
              apagar();
              Serial.println("Cliente Desconectado");
              Serial.println("Cliente Desconectado");
              numero1();
            } else if (Estado==2){
              apagar();
              numero2();
            } else if (Estado==3){
              apagar();
              numero3();
            } else if (Estado==4){
              apagar();
              numero4();
            } else if (Estado==5){
              apagar();
              numero5();
            } else if (Estado==6){
              apagar();
              numero6();
            } else if (Estado==7){
              apagar();
              numero7();
            } else if (Estado==8){
              apagar();
              numero8();
            } else if (Estado==9){
              apagar();
              numero9();
              Serial.println("Cliente Desconectado");
              Serial.println("Cliente Desconectado");
              Serial.println("Cliente Desconectado");
            } else if (Estado==10){
              apagar();
              Serial.println("Cliente ASDASDASDASD");
            }
            ResponderCliente(cliente);
            break;
          } else {
            Serial.println(LineaActual);
            VerificarMensaje(LineaActual);
            LineaActual = "";
          }
        }  else if (Letra != '\r') {
          LineaActual += Letra;
        }
      }
    }

    cliente.stop();
    Serial.println("Cliente Desconectado");
    Serial.println();
  }
}

void VerificarMensaje(String Mensaje) {
  if (Mensaje.indexOf("GET /0") >= 0) {
    Serial.println("Encender Led");
    Estado = 0;
  } else if (Mensaje.indexOf("GET /1") >= 0) {
    Serial.println("Apagar Led");
    Estado = 1;
  }  else if (Mensaje.indexOf("GET /2") >= 0) {
    Serial.println("Apagar Led");
    Estado = 2;
  } else if (Mensaje.indexOf("GET /3") >= 0) {
    Serial.println("Apagar Led");
    Estado = 3;
  } else if (Mensaje.indexOf("GET /4") >= 0) {
    Serial.println("Apagar Led");
    Estado = 4;
  } else if (Mensaje.indexOf("GET /5") >= 0) {
    Serial.println("Apagar Led");
    Estado = 5;
  } else if (Mensaje.indexOf("GET /6") >= 0) {
    Serial.println("Apagar Led");
    Estado = 6;
  } else if (Mensaje.indexOf("GET /7") >= 0) {
    Serial.println("Apagar Led");
    Estado = 7;
  } else if (Mensaje.indexOf("GET /8") >= 0) {
    Serial.println("Apagar Led");
    Estado = 8;
  } else if (Mensaje.indexOf("GET /9") >= 0) {
    Serial.println("Apagar Led");
    Estado = 9;
  } else if (Mensaje.indexOf("GET /10") >= 0) {
    Serial.println("Apagar Led");
    Estado = 10;
  }
}

void ResponderCliente(WiFiClient& cliente) {
  cliente.print(Pagina);
  cliente.print("Hola ");
  cliente.print(cliente.remoteIP());
  cliente.print("<br>Estado del led: ");
  cliente.print(Estado);
  cliente.print("<br>Cambia el Led: <br>");
  for(int i = 0; i <10; i++){
    cliente.print("<br><a href = '/");
    cliente.print(i);
    cliente.print("'>BOTON");
    cliente.print(i);
    cliente.print("</a><br>");
  }
  cliente.print("<br><a href = '/20'>BOTON</a><br>");
  cliente.print("</html>");
}

#define D0 16
#define D1 05
#define D2 04
#define D3 00
#define D4 02
#define D5 14
#define D6 12

void numero0() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
}
 
void numero1() {
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
}

void numero2() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D6, HIGH);
}

void numero3() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D6, HIGH);
}

void numero4() {
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
}

void numero5() {
  digitalWrite(D0, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
}

void numero6() {
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
}

void numero7() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
}

void numero8() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
}

void numero9() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
}

void apagar() {
  digitalWrite(D0, LOW);
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW);
  digitalWrite(D3, LOW);
  digitalWrite(D4, LOW);
  digitalWrite(D5, LOW);
  digitalWrite(D6, LOW);
}
