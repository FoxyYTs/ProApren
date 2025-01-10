#include <DHT.h>
#include <DHT_U.h>

DHT dht(D1, DHT11);

float temp, hume;

void setup() {
  Serial.begin(9600);
  dht.begin();

}

void loop() {
  hume = dht.readHumidity();
  temp = dht.readTemperature();

  Serial.println("Temperatura: " + String(temp));
  Serial.println("Humedad: " + String(hume));

  delay(1000);

}
