#include <avr/io.h>
//#define CARD_CHECK1()((PINC & (1<<PC3)) == 0) 
//#define CARD_CHECK2()((PINC & (1<<PC4)) == 0)

#define REED0() (PINC & (1<<PC0) == 0)
#define REED1() (PINC & (1<<PC1) == 0)
#define REED2() (PINC & (1<<PC2) == 0)
#define REED3() (PINC & (1<<PC3) == 0)

void init_peri();
void set_led_value(uint8_t value);
void buzzer(int value);
uint16_t read_adc(uint8_t channel);
