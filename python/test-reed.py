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


while True:

    r0 = peri.reed_0()          # read REED 0
    r1 = peri.reed_1()          # read REED 1
    r2 = peri.reed_2()          # read REED 2
    r3 = peri.reed_3()          # read REED 3
    card = peri.check_card()    # check if card placed
    print(f"{r0} {r1} {r2} {r3} => card: {card}")

    if (r1 or r2 or r3 or r4):
        peri.buzzer_on()

        peri.led_off_red()
        peri.led_on_green()

        time.sleep(0.2)
        peri.buzzer_off()

    else:
        peri.led_off_green()
        peri.on_red()
    time.sleep(0.4)

