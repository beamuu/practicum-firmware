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
    reed_state_0 = peri.reed_0()
    reed_state_1 = peri.reed_1()
    reed_state_2 = peri.reed_2()
    reed_state_3 = peri.reed_3()
    print(f"{reed_state_0} {reed_state_1} {reed_state_2} {reed_state_3}")
    time.sleep(1)
