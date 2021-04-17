from practicum import find_mcu_boards , McuBoard , PeriBoard
import time
devices = find_mcu_boards()
print(f"found {len(devices)}")

for i in devices:
    print(f"    {i}")
    
mcu = McuBoard(devices[0])
print("__________________________")
print(f"__selected {devices[0]}")
peri = PeriBoard(mcu)

peri.led_on_red()

while True:

    r0 = peri.reed0()          # read REED 0
    r1 = peri.reed1()          # read REED 1
    r2 = peri.reed2()          # read REED 2
    r3 = peri.reed3()          # read REED 3
    card = peri.check_card()    # check if card placed
    print(f"{r0} {r1} {r2} {r3} => card: {card}")

    if (r0 or r1 or r2 or r3):
        peri.buzzer_on()

        peri.led_off_red()
        peri.led_on_green()

        time.sleep(0.2)
        peri.buzzer_off()
        time.sleep(0.5) 
        peri.led_off_green()
        peri.led_on_red()

    time.sleep(0.4)

