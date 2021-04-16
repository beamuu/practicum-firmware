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
    reed_state = peri.get_reed_id()
    print(reed_state)
    time.sleep(1)
