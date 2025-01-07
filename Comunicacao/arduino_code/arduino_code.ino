#include <math.h>

String cmd;
char byteRead;
String sensors[5];
int values[5];

void setup(){
  Serial.begin(9600);
  sensors[0]="S1";
  sensors[1]="S2";
  sensors[2]="S3";
  sensors[3]="S4";
  sensors[4]="S5";

  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(7, INPUT);
  pinMode(2, OUTPUT);
}

void readAllSensor(){
    values[0]=analogRead(A0);
    values[1]=analogRead(A1);
    values[2]=analogRead(A2);
    values[3]=digitalRead(7);
    values[4]=random(0,1023);

    for (int i=0;i<4;i++){
      Serial.print(values[i]);
      Serial.print(" ");
    }
    Serial.println(values[4]);
    delay(10);
}

int t=0;
float d1,d2,d3;
void loop(){
    cmd="";
    while (Serial.available()>0){
      byteRead = Serial.read();
      cmd+=byteRead;
      delay(1);
    }
    // Evaluate command
    if (cmd.substring(0,1) == "#"){readAllSensor();}
    delay(10);
}
