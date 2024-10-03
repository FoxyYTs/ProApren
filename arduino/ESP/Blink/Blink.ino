#define D0 16
#define D1 05
#define D2 04
#define D3 00
#define D4 02
#define D5 14
#define D6 12
#define time 1000

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  pinMode(D5, OUTPUT);
  pinMode(D6, OUTPUT);
}
void numero0() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
  delay(time);
}
 
void numero1() {
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  delay(time);
}

void numero2() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
}

void numero3() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
}

void numero4() {
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
}

void numero5() {
  digitalWrite(D0, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
}

void numero6() {
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
}

void numero7() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  delay(time);
}

void numero8() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
}

void numero9() {
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D5, HIGH);
  digitalWrite(D6, HIGH);
  delay(time);
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

void test() {
  digitalWrite(D0, HIGH);
  delay(time);    
  digitalWrite(D1, HIGH);
  delay(time);
  digitalWrite(D2, HIGH);
  delay(time);    
  digitalWrite(D3, HIGH);
  delay(time);
  digitalWrite(D4, HIGH);
  delay(time);
  digitalWrite(D5, HIGH);
  delay(time);    
  digitalWrite(D6, HIGH);
  delay(time);
  digitalWrite(D7, HIGH);
  delay(time);    
  digitalWrite(D8, HIGH);
  delay(time);
  digitalWrite(D0, LOW);
  delay(time);   
  digitalWrite(D1, LOW);
  delay(time);
  digitalWrite(D2, LOW);
  delay(time);   
  digitalWrite(D3, LOW);
  delay(time);
  digitalWrite(D4, LOW);
  delay(time);
  digitalWrite(D5, LOW);
  delay(time);   
  digitalWrite(D6, LOW);
  delay(time);
  digitalWrite(D7, LOW);
  delay(time);   
  digitalWrite(D8, LOW);
  delay(time);
}

// the loop function runs over and over again forever
void loop() {
  numero0();
  apagar();
  numero1();
  apagar();
  numero2();
  apagar();
  numero3();
  apagar();
  numero4();
  apagar();
  numero5();
  apagar();
  numero6();
  apagar();
  numero7();
  apagar();
  numero8();
  apagar();
  numero9();
  apagar();
}  
