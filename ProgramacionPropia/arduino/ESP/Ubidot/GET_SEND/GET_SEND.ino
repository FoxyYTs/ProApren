#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
const int Sensor = 7;
const int Bomba = 13;

//Crear el objeto lcd  dirección  0x3F y 16 columnas x 2 filas
LiquidCrystal_I2C lcd(0x20,16,2);  //



void setup() {
  Serial.begin(9600);
  pinMode(Bomba, OUTPUT);
  // Inicializar el LCD
  lcd.init();
  
  //Encender la luz de fondo.
  lcd.backlight();
  
  // Escribimos el Mensaje en el LCD.
  llenado();
}

void loop() {
  long duration, cm;

  pinMode(Sensor, OUTPUT);
  digitalWrite(Sensor, LOW);
  delayMicroseconds(2);
  digitalWrite(Sensor, HIGH);
  delayMicroseconds(5);
  digitalWrite(Sensor, LOW);
  
  pinMode(Sensor, INPUT);
  duration = pulseIn(Sensor, HIGH);

  
  cm = microsecondsToCentimeters(duration);

  
  Serial.print("Distance: ");
  Serial.print(cm);
  Serial.print("cm");
  Serial.println();
  
  if(cm <= 100) {//Modificar para determinar la distancia de activacion
    llenado();
  }
  else {
    espera();
  }
}

void espera() {
  digitalWrite(Bomba, LOW);
  lcd.setCursor(0,0);
  lcd.print("BOMBA APAGADA  ");
  lcd.setCursor(0,1);
  lcd.print("Esperando vaso");
  delay(10);
  
}

void llenado() {
  digitalWrite(Bomba, HIGH);
  lcd.setCursor(0,0);
  lcd.print("ACTIVANDO BOMBA");
  lcd.setCursor(0,1);
  lcd.print("Llenando vaso ");
  delay(10);
}

long microsecondsToCentimeters(long microseconds) {
  
  return microseconds / 29 / 2;
}