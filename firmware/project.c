#define F_CPU 16000000
#include <stdio.h>
#include <avr/io.h>
#include <util/delay.h>
#include "meg.h"

int main() {

  init_peri();
  set_led_value(0);
  int status;
  int id;
  //buzzer(0);
//   while(1) {

//     set_led_value(0b01);

//     id = 0;
//     status = 0;
//     //while (!CARD_CHECK1()) {}

//     //_delay_ms(1000);

//     while (!CARD_CHECK1()) {}

//     _delay_ms(50);

//     status = 1;

//     set_led_value(0b10);

//     PINC |= (1<<PC2);
//     _delay_ms(100);
//     PORTC &= 0b11111011;
//     _delay_ms(50);
//     PINC |= (1<<PC2);
//     _delay_ms(200);
//     PORTC &= 0b11111011;
//     _delay_ms(1000);

//     if(PORTB & (0b00001111)) {
//         id += 8;
//     }

//     if(PORTB & (0b00000100)) {
//         id += 4;
//     }

//     if(PORTB & (0b00000010)) {
//         id += 2;
//     }

//     if(PORTB & (0b00000001)) {
//         id += 1;
//     }


//     while (CARD_CHECK1()) {}

//     _delay_ms(50);

//   }

    while (1) {
        while (!(REED0()||REED1()||REED2()||REED3())) {}

        _delay_ms(50);
        PINC |= (1<<PC4);
    _delay_ms(100);
    PORTC &= 0b11101111;
    _delay_ms(50);
    PINC |= (1<<PC4);
    _delay_ms(200);
    PORTC &= 0b11101111;
    _delay_ms(1000);

    

    while ( (REED0()||REED1()||REED2()||REED3())) {}

    _delay_ms(50);
    }
}