#include<Arduino.h>
int A=0,B=0;
int DIFFERENCE,BORROW;


void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
   
}


void loop() {
  
 DIFFERENCE=(!A&&B) || (!B&&A);
BORROW=(!A&&B);

  digitalWrite(2, DIFFERENCE); 
  digitalWrite(3, BORROW); 
  }
