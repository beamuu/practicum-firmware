#include <avr/io.h>
#include "meg.h"

void init_peri() {
    // PC0..PC2 -> output
    // PC3,PC4 -> input

    //   DDRC |= (1<<PC2) | (1<<PC1) | (1<<PC0);
    //   DDRC &= ~((1<<PC3)|(1<<PC4));

//   PORTC |= (1<<PC3);
 
    // for test only
    DDRC &= ~((1<<PC0)|(1<<PC1)|(1<<PC2)|(1<<PC3));
}




void set_led_value(uint8_t value) {
  PORTC &= ~(0b11);
  PORTC |= (value & 0b11);
}

void buzzer(int value) {
  PORTC |= (value<<PC2);
}

uint16_t read_adc(uint8_t channel) {
  ADMUX = (0<<REFS1)|(1<<REFS0) // ระบใหใช VCC เปนแรงดนอางอง (Vref) และ
    | (0<<ADLAR)            // บนทกผลลพธชดขวาในครจสเตอร ADCH/ADCL
    | (channel & 0b1111);   // ตงคา MUX เปนคา channel

  ADCSRA = (1<<ADEN)            // เปดวงจร ADC
    | (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) // ใชความเรว 1/128 ของคลอกระบบ
    | (1<<ADSC);           // สงวงจร ADC ใหเรมตนการแปลง

  while ((ADCSRA & (1<<ADSC)))  // รอจนบต ADSC กลายเปน 0 ซงหมายถงการแปลงเสรจสน
    ;

  return ADCL + ADCH*256;  // ผลลพธถกเกบอยในรจสเตอร ADCL และ ADCH

}