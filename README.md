# Practicum Project "Authy (firmware only)"
This project is hosted on `Heroku`, https://practicum-po.herokuapp.com.

### About

This project is a part of Practicum's final project, Department of Computer Engineering, Kasetsart University.<br>
Academic Year 2020

- website details:  https://practicum-po.herokuapp.com/about

created by **Po the Dragon Warrior** group (โปนักมังกร)
- Chalanthorn Aenguthaivadt `6210503527`
- Nutchanon Chantrasup `6210503578`
- Napasin Saengthong `6210503641`
- Nik Kunraho Struyf `6210506500`

### Components
`firmware/main.c` main program for firmware and hardware initializer.
`python/practicum.py` includes classes for control hardware
  - `find_mcu_boards`
  - `McuBoard`
  - `PeriBoard`
 
`python/test-reed.py` main program for controlling hardware with python which will calls a firmware later.

### Running the project in KU Raspberry Pi
  - `make flash` at `firmware/`
  - `. ~/virtualenv/practicum/bin/activate`
  - `python3 python/test-reed.py`
  

