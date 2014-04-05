
// photo resistors
int LDR_Pin0 = A1; //analog pin 0
int LDR_Pin1 = A2; //analog pin 1
int LDR_Pin2 = A3; //analog pin 2
int LDR_Pin3 = A4; //analog pin 3


#define IRpin_PIN      PIND
#define IRpin          2
int IRledPin =  3;             // LED connected to digital pin 3
int REDledPin = 6;             // LED connected to digital pin 3
int GRNledPin = 5;             // LED connected to digital pin 3
int YELledPin = 7;             // LED connected to digital pin 3

void setup()                    // run once, when the sketch starts
{
  pinMode(IRledPin, OUTPUT);   
  pinMode(REDledPin, OUTPUT);   
  pinMode(GRNledPin, OUTPUT);   
  pinMode(YELledPin, OUTPUT);
  Serial.begin(115200);           // set up Serial library at 9600 bps  
}


void pulseIR(long microsecs) {
  // we'll count down from the number of microseconds we are told to wait
 
  cli();  // this turns off any background interrupts
 
  while (microsecs > 0) {
    // 38 kHz is about 13 microseconds high and 13 microseconds low
   digitalWrite(IRledPin, HIGH);  // this takes about 3 microseconds to happen
   delayMicroseconds(9);         // hang out for 10 microseconds, you can also change this to 9 if its not working
   digitalWrite(IRledPin, LOW);   // this also takes about 3 microseconds
   delayMicroseconds(9);         // hang out for 10 microseconds, you can also change this to 9 if its not working
 
   // so 26 microseconds altogether
   microsecs -= 26;
  }
  sei();  // this turns them back on
}


int cur_pulse_count = -1;
uint16_t pulses[600];
void transmitPulses() {  
  for (int i=0; i<(cur_pulse_count/2); i++) {    
    pulseIR(pulses[i*2]*10);
    delayMicroseconds(pulses[i*2+1]*10);
  }
}

void printPulses() {
  for (int i=0; i<(cur_pulse_count/2); i++) {    
    Serial.print(pulses[i*2]);
    Serial.print(",");
    Serial.print(pulses[i*2+1]);
    Serial.print("; ");
  }
  Serial.println(";;;");
}

int TIMEOUT=200;
int incomingByte = 0;
int incomingByte2 = 0;
int STARTER = 1313;
int FINISHER = 1414;
long last_read = 0;
long start_read = 0;
int readIntFromBytes() {
  union u_tag {
    byte b[2];
    int ulval;
  } u;
  u.b[0] = Serial.read();
  u.b[1] = Serial.read();
  return u.ulval;
}

int OK_timeout = 3000;
long last_OK = 0;
long last_sensor_reading;
long last_sensor_broadcast;
int sensor_timeout_broadcast = 1000; //report every 1s
int sensor_timeout_reading = 100; //sample every 100ms

int ON_THRESHOLD = 500;
int LIGHT_DIFF = 100;
int LDRReading0 = 0;
int LDRReading1 = 0;
int LDRReading2 = 0;
int LDRReading3 = 0;

void loop() {
    
    // sample interval
    if (cur_pulse_count == -1 && millis() - last_sensor_reading > sensor_timeout_reading) {
      LDRReading0 = analogRead(LDR_Pin0); 
      LDRReading1 = analogRead(LDR_Pin1); 
      LDRReading2 = analogRead(LDR_Pin2);  // light reference - should be dark
      LDRReading3 = analogRead(LDR_Pin3);   
      
      // 0 is reference reading
      // 1 is on/off (on if in operation)
      // 2 is standy (always on)
      // 3 is outside
      digitalWrite(REDledPin, LDRReading1 - LDRReading0 > LIGHT_DIFF);
      digitalWrite(GRNledPin, LDRReading2 - LDRReading0 > LIGHT_DIFF);
      
      last_sensor_reading = millis();
    }
    
    // only transmit sensor reading when not in the middle of receiving a packet,
    // otherwise wait for the next cycle
    if (cur_pulse_count == -1 && millis() - last_sensor_broadcast > sensor_timeout_broadcast) {
      Serial.print("L0:"); Serial.print(LDRReading0); Serial.print(";");
      Serial.print("L1:"); Serial.print(LDRReading1); Serial.print(";");
      Serial.print("L2:"); Serial.print(LDRReading2); Serial.print(";"); 
      Serial.print("L3:"); Serial.print(LDRReading3); Serial.println(";");      
      last_sensor_broadcast = millis();
    }  
  
    // keep-alive information
    if (cur_pulse_count == -1 && millis() - last_OK > OK_timeout) {
        Serial.println("IR sender OK");
        last_OK = millis();
    }

    //reset waiting for packet
    if (cur_pulse_count != -1 && millis() - last_read > TIMEOUT) {
       cur_pulse_count = -1;
       Serial.println("X: incomplete-abort;");
    }
    // we have data
    if (Serial.available() > 1) {      
        //two bytes at once..
        incomingByte = readIntFromBytes();  
        if (cur_pulse_count == -1) {
            // check for start char
            if (incomingByte == STARTER) {
              //let's continue
              start_read = millis();
              cur_pulse_count = 0;
              Serial.println("X: start");
            } 
        } else {
            if (incomingByte == FINISHER) {
                digitalWrite(YELledPin, HIGH);
                Serial.println("Command received");
                transmitPulses();
                printPulses();
                digitalWrite(YELledPin, LOW);
                Serial.println("Time taken:");
                Serial.print(millis() - start_read, DEC);
                Serial.println(" millis");
                // reset pulse counter
                cur_pulse_count = -1;
                // wait a bit for good measure
                delay(500);
            } else {
                // fill the buffer
                Serial.print("*:");
                pulses[cur_pulse_count] = incomingByte;
                cur_pulse_count++;
            }
        }
        // mark last read
        last_read = millis();
    }    
}




