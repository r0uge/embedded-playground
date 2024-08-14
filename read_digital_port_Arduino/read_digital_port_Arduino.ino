//Microcontrolador: Arduino
//Descripción:
//  Lee un puerto digital y lo muestra en la salida serie
//Autor: Agustin Alvarez
//Fecha: 14/8/2024

int IRSensor = 9; // connect IR sensor module to Arduino pin D9

void setup(){
  Serial.begin(115200); // Init Serial at 115200 Baud Rate.
  Serial.println("Serial Working"); // Test to check if serial is working or not
  pinMode(IRSensor, INPUT); // IR Sensor pin INPUT
}

void loop(){
  int sensorStatus = digitalRead(IRSensor); // Set the GPIO as Input
  if (sensorStatus == 1) // Check if the pin high or not
  { 
    Serial.println("Señal Recibida!!"); // print  on the serial monitor window
  }
}