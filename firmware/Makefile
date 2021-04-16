TARGET=main
MCU=atmega328p
F_CPU=16000000
CFLAGS=-mmcu=$(MCU) -Wall -Os -DF_CPU=$(F_CPU) -Iusbdrv -I.
OBJS=peri.o usbdrv/usbdrv.o usbdrv/usbdrvasm.o

.SECONDARY:

all: $(TARGET).hex

flash: $(TARGET).flash

%.flash: %.hex
	avrdude -p $(MCU) -c usbasp -u -U flash:w:$<

%.hex: %.elf
	avr-objcopy -j .text -j .data -O ihex $< $@

%.elf: %.o $(OBJS)
	avr-gcc $(CFLAGS) -o $@ $^

%.o: %.c usbconfig.h
	avr-gcc $(CFLAGS) -c -o $@ $<

%.o: %.S
	avr-gcc $(CFLAGS) -x assembler-with-cpp -c -o $@ $<

clean:
	rm -f *~
	rm -f *.o
	rm -f *.elf
	rm -f *.hex
	rm -f $(OBJS)
	rm -f $(TARGET)
