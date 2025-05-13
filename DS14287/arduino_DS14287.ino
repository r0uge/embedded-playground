const int dataPins[] = {2, 3, 4, 5, 6, 7, 8, 9}; // D0 to D7
const int A0_PIN = 10;
const int A1_PIN = 11;
const int RW_PIN = 12;
const int CS_PIN = 13;
const int DS_PIN = A0;
const int AS_PIN = A1;
const int RESET_PIN = A2;

void setup() {
  Serial.begin(9600);

  pinMode(CS_PIN, OUTPUT);
  pinMode(DS_PIN, OUTPUT);
  pinMode(AS_PIN, OUTPUT);
  pinMode(RW_PIN, OUTPUT);
  pinMode(A0_PIN, OUTPUT);
  pinMode(A1_PIN, OUTPUT);
  pinMode(RESET_PIN, OUTPUT);

  digitalWrite(RESET_PIN, HIGH); // Activar chip
  digitalWrite(CS_PIN, LOW);     // Seleccionado
  digitalWrite(AS_PIN, HIGH);
  digitalWrite(DS_PIN, HIGH);
}

void loop() {
  byte reg = 0x00; // Registro de segundos
  byte value = readRTCRegister(reg);
  Serial.print("Valor de reg ");
  Serial.print(reg, HEX);
  Serial.print(": ");
  Serial.println(value, HEX);

  delay(1000);
}

byte readRTCRegister(byte reg) {
  // Establecer dirección
  digitalWrite(A0_PIN, bitRead(reg, 0));
  digitalWrite(A1_PIN, bitRead(reg, 1));

  // Ciclo de dirección
  digitalWrite(AS_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(AS_PIN, HIGH);

  // Leer datos
  for (int i = 0; i < 8; i++) {
    pinMode(dataPins[i], INPUT);
  }

  digitalWrite(RW_PIN, HIGH); // Modo lectura
  digitalWrite(DS_PIN, LOW);
  delayMicroseconds(2);

  byte value = 0;
  for (int i = 0; i < 8; i++) {
    bitWrite(value, i, digitalRead(dataPins[i]));
  }

  digitalWrite(DS_PIN, HIGH);

  return value;
}
