int cc=0;
void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT); 
  pinMode(4, INPUT); 
  pinMode(5, INPUT); 
  pinMode(10, INPUT); 
  pinMode(11, INPUT); 
  pinMode(12, INPUT); 
  pinMode(13, INPUT);
  Serial.begin(9600);                       // set the baud rate
  //Serial.println("Ready");                  // print "Ready" once
   }
void loop() {

int z0 = digitalRead(2);
int z1 = digitalRead(3);
int z2 = digitalRead(4);
int z3 = digitalRead(5);
int z4 = digitalRead(10);
int z5 = digitalRead(11);
int z6 = digitalRead(12);
int z7 = digitalRead(13);
int no = (z7<<7)+(z6<<6)+(z5<<5)+(z4<<4)+(z3<<3)+(z2<<2)+(z1<<1)+z0;
Serial.println(int(no));
              delay(1000);
  }

 // if(cc==0){
//
  //  cc=1;
  
    
  
