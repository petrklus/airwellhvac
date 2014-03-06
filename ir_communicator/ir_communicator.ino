#define IRpin_PIN      PIND
#define IRpin          2
int IRledPin =  3;    // LED connected to digital pin 13
void setup()                    // run once, when the sketch starts
{
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
    Serial.println(pulses[i*2+1]);
  }
}

int TIMEOUT=100;
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

void loop() {
    
    //reset waiting for packet
    if (millis() - last_read > TIMEOUT) {
        cur_pulse_count = -1;
        //Serial.println("Abort");
    }
    
    // we have data
    if (Serial.available() > 1) {
        //two bytes at once..
        incomingByte = readIntFromBytes();  
//        Serial.print("received");
//        Serial.println(incomingByte, DEC);
        if (cur_pulse_count == -1) {
            // check for start char
            if (incomingByte == STARTER) {
              //let's continue
              start_read = millis();
              cur_pulse_count = 0;
            } 
        } else {
            if (incomingByte == FINISHER) {
                Serial.println("Command received");
                printPulses();
                Serial.println("Time taken:");
                Serial.print(millis() - start_read, DEC);
                Serial.println(" millis");
                // reset pulse counter
                cur_pulse_count = -1;
            } else {
                // fill the buffer
                pulses[cur_pulse_count] = incomingByte;
                cur_pulse_count++;
            }
        }
        // mark last read
        last_read = millis();
    }    
}




