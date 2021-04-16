#include <avr/io.h>
#include "peri.h"

void init_peri()
{
    // PC0..PC2 -> output
    DDRC |= (1<<PC2)|(1<<PC1)|(1<<PC0);

    // PC3,PC4 -> input
    DDRC &= ~((1<<PC3)|(1<<PC4));

    // enable pull-up resistor on PC3
    PORTC |= (1<<PC3);

    // turn off all LEDs
    set_led_value(0);
}

void set_led(uint8_t pin, uint8_t state)
{
    if (pin > 2) return;
    if (state)
        PORTC |= (1<<pin);
    else
        PORTC &= ~(1<<pin);
}

void set_led_value(uint8_t value)
{
    PORTC &= ~(0b111);
    PORTC |= (value & 0b111);
}

uint16_t read_adc(uint8_t channel)
{
    ADMUX = (0<<REFS1)|(1<<REFS0) // use VCC as reference voltage
          | (0<<ADLAR)            // store result to the right of ADCH/ADCL
          | (channel & 0b1111);   // point MUX to the specified channel
 
    ADCSRA = (1<<ADEN)            // enable ADC
           | (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) // set speed to 1/128 of system clock
           | (1<<ADSC);           // start conversion
 
    // wait until ADSC bit becomes 0, indicating complete conversion
    while ((ADCSRA & (1<<ADSC)))
       ;
 
    return ADCL + ADCH*256;
}
