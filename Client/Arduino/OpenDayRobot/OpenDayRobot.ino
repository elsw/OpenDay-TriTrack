int val = 0; 
int count = 0;
int AReadCount = 6;
int AReadPins[] = {2,3,4,5,6,7};

int outPinCount = 10;
int outPins[] = {53,51,49,47,45,43,41,39,37,35};
int addrPinCount = 4;
int addrOutPins[] = {33,31,29,27};
int validPin = 25;
int readyPin = 23;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  for( int n=0 ; n < outPinCount ; n++){ 
    pinMode(outPins[n], OUTPUT);
  }
  for( int n=0 ; n < addrPinCount ; n++){ 
    pinMode(addrOutPins[n], OUTPUT);
  }
  pinMode(validPin,OUTPUT);
  pinMode(readyPin,INPUT);

  digitalWrite(validPin,0);
}

void loop() {
  // put your main code here, to run repeatedly:
   val = analogRead(AReadPins[count]);    // read the input pin
    //Serial.println(val);             // debug value

    //output readings in parallel
    digitalWrite(validPin,0);
    delay(2);
    outputData(val);
    outputAddress(AReadPins[count]);
    delay(2);
    digitalWrite(validPin,1);    
    
    //increase address counter
    count++;
    if(count >= AReadCount){
      count = 0;
    }

    //wait for ready signal form pi
    while(!digitalRead(readyPin));
}

//takes between 0 and 1024
void outputData(int i){
  for(int n=0 ; n < outPinCount ; n++ ){
    digitalWrite(outPins[n], bitRead(i,n));
  }
}
void outputAddress(int i){
  for(int n=0 ; n < addrPinCount ; n++ ){
    digitalWrite(addrOutPins[n], bitRead(i,n));
  }
}

