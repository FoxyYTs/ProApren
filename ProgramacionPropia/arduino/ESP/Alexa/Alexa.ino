
//#define ESPALEXA_DEBUG            //Activa depuraccion

#if defined(ESP32)
#include <WiFi.h>
#else
#include <ESP8266WiFi.h>

#endif
#include <Espalexa.h>

const char* ssid = "TP-LINK_0C96";
const char* password = "LabIntegrado101";

Espalexa miAlexa;
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

void cambiarLampara(uint8_t brillo) {
  Serial.print("Cambiando Lampara a: ");
  float x = (float)brillo/255;
  Serial.println(x);

  if (x > 0 && x < 0.1)
  {
    Serial.print("Numero 0, brillo ");
    Serial.println(brillo);
    apagar();
    numero0();
  } 
  else if (x >= 0.1 && x < 0.2)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero1();
  }
  else if (x >= 0.2 && x < 0.3)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero2();
  }
  else if (x >= 0.3 && x < 0.4)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero3();
  }
  else if (x >= 0.4 && x < 0.5)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero4();
  }
  else if (x >= 0.5 && x < 0.6)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero5();
  }
  else if (x >= 0.6 && x < 0.7)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero6();
  }
  else if (x >= 0.7 && x < 0.8)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero7();
  }
  else if (x >= 0.8 && x < 0.9)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero8();
  }
  else if (x >= 0.9 && x <= 1)
  {
    Serial.print("Encendido, brillo ");
    Serial.println(brillo);
    apagar();
    numero9();
  }
  else
  {
    Serial.println("Apagado");
    apagar();
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
  apagar();
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");
  Serial.println("Iniciar sistema");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Conectado a ");
  Serial.println(ssid);
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  miAlexa.addDevice("foco", cambiarLampara);
  miAlexa.begin();

}

void loop() {
  // Alexa, busca dispositivos
  miAlexa.loop();
  delay(1);
}