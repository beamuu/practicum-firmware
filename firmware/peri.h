#define SWITCH_PRESSED() ((PINC & (1<<PC3)) == 0)

void init_peri();
void set_led(uint8_t pin, uint8_t state);
void set_led_value(uint8_t value);
uint16_t read_adc(uint8_t channel);
