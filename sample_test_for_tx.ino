void setup() {
  pinMode(6, OUTPUT); 
  pinMode(7, OUTPUT); 
  pinMode(8, OUTPUT); 
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);                       // set the baud rate
    }
   void loop(){
int value=40;
    
        bool b7 = value%2;
        value = (value>>1);
        bool b6 = value%2;
        value = (value>>1);
        bool b5 = value%2;
        value = (value>>1);
        bool b4 = value%2;
        value = (value>>1);
        bool b3 = value%2;
        value = (value>>1);
        bool b2 = value%2;
        value = (value>>1);
        bool b1 = value%2;
        value = (value>>1);
        bool b0 = value%2;
        digitalWrite(13,b7);
        digitalWrite(12,b6);
        digitalWrite(11,b5);
        digitalWrite(10,b4);
        digitalWrite(9,b3);
        digitalWrite(8,b2);
        digitalWrite(7,b1);
        digitalWrite(6,b0);

      //} else if (pos < sizeof buffer - 1) {   // otherwise, buffer it
     // buffer[pos++] = c;
  
   //}
}
