from practicum import find_mcu_boards , McuBoard , PeriBoard
import time
devices = find_mcu_boards()
mcu = McuBoard(devices[0])
peri = PeriBoard(mcu)


while True:
    reed_state = peri.get_reed_id()
    print(reed_state)
    time.sleep(1)
