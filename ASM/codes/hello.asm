.include "/home/user/m328Pdef.inc"
Start:
 ldi r30,0b11111100;     \\identifying input 8,9
 out DDRB,r30;            \\declaring pins as input
 ldi r30,0b11111111;
 out PORTB,r30;            \\activating internal-pullup for pins 8,9
 in r30,PINB
 ldi r16,0b00001100;        \\identifying output pin 2,3
 out DDRD,r16;
 ldi r17,0b00000001 
 ldi r18,0b00000001
 ldi r19,0b00000001
 ldi r20,0b00000001

AND r17,r30 ;r17=B
LSR  r30

AND r18,r30 ;r18=A

EOR r19,r17 ;r19=B'

EOR r20,r18 ;r20=A'

mov r30,r20
AND r30,r17 ;r30=A'B

mov r31,r18
AND r31,r19 ;r31=AB'

OR r31,r30 ;r31=AB'+A'B

LSL r31

OR r31, r30 ;pin3=D,pin2=B

out  PORTD,r31

rjmp Start
