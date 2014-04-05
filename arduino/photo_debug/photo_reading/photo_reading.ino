int LDR_Pin0 = A0; //analog pin 0
int LDR_Pin1 = A1; //analog pin 0
int LDR_Pin2 = A2; //analog pin 0
//int LDR_Pin3 = A3; //analog pin 0

#include <SmoothAnalogInput.h>
#define SMOOTH_ANALOG_INPUT_SIZE 32


void setup(){
  Serial.begin(115200);
}

void loop(){
  int LDRReading0 = analogRead(LDR_Pin0); 
  int LDRReading1 = analogRead(LDR_Pin1); 
  int LDRReading2 = analogRead(LDR_Pin2); 
//  int LDRReading3 = analogRead(LDR_Pin3); 
  
  Serial.print(LDRReading0); Serial.print(", ");
  Serial.print(LDRReading1); Serial.print(", ");
  Serial.print(LDRReading2); Serial.print(", ");  
  
  Serial.println(".");  
  delay(500); //just here to slow down the output for easier reading
}
