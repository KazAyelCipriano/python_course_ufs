#include <math.h>

String cmd;
char byteRead;

void setup(){
  Serial.begin(9600);
}

int t=0;
float d1,d2,d3;
void loop(){
    d1=3*sin(0.2*t)+1+random(0,1);
    d2=2*sin(0.1*t)+3+random(0,0.5);
    d3=5*sin(0.2*t)+random(0,2);
    t=t+1;    
    Serial.print(d1);
    Serial.print(" ");
    Serial.print(d2);
    Serial.print(" ");
    Serial.println(d3);
    
    delay(10);
    cmd="";
    while (Serial.available()>0){
      byteRead = Serial.read();
      cmd+=byteRead;
      delay(1);
    }
    //Serial.println(cmd);
    // Gets command
    if (cmd.substring(0,1) == "#" & cmd.length()==13){
      for (int i=1;i<13;i++){
        if (cmd.substring(i,i+1)=="1"){digitalWrite(1+i,HIGH);}
        else{digitalWrite(1+i,LOW);}
      }
    }
}
