#include <avr/io.h>
#define CARD_CHECK1()((PINC & (1<<PC3)) == 0)
#define CARD_CHECK2()((PINC & (1<<PC4)) == 0)
#define REED() (~(PINB & 0b00001111))
void init_peri();
void set_led_value(uint8_t value);
void buzzer(int value);
uint16_t read_adc(uint8_t channel);