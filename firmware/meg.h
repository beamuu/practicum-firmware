#include <avr/io.h>
#define CARD_CHECK1()((PINC & (1<<PC3)) == 0)
#define REED0() ((PINB & (1<<PB0)) == 0)
#define REED1() ((PINB & (1<<PB1)) == 0)
#define REED2() ((PINB & (1<<PB2)) == 0)
#define REED3() ((PINB & (1<<PB3)) == 0)
#define buzzer_on() (PINC |= (1<<PC2))
#define buzzer_off() (PORTC &= 0b11111011)
#define led_on_green() (PINC |= (1<<PC1))
#define led_on_red() (PINC |= (1<<PC0))
#define led_off_green() (PORTC &= 0b11111101)
#define led_off_red() (PORTC &= 0b11111110)
void init_peri();
