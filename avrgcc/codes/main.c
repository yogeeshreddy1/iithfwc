#include <avr/io.h>
#include <stdbool.h>
#include <util/delay.h>
int main (void)
{

 bool a=0,b=0,difference=0,borrow=0;
 DDRB =  0b00110000;  //12 and  13 pin as output 
 DDRD =  0b11110011;
 PORTD = 0b00001100;   // 2,3 as inputs
 

while(1)
{  

a= (PIND & (1 << PIND2)) == (1 << PIND2);
b= (PIND & (1 << PIND3)) == (1 << PIND3);
difference=((!a&b)|(!b&a));
borrow=(!a&b);
PORTB |= (difference<< 5);
_delay_ms(500);
PORTB |= (borrow<< 4);
_delay_ms(500);
}
return 0;
}
