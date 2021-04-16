from practicum import find_mcu_boards, McuBoard, PeriBoard

devices = find_mcu_boards()
mcu = McuBoard(devices[0])
peri = PeriBoard(mcu)
