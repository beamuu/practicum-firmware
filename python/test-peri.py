import usb
from practicum import find_mcu_boards, McuBoard, PeriBoard
from time import sleep

devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

mcu = McuBoard(devs[0])
print("*** Practicum board found")
print("*** Manufacturer: %s" % \
        mcu.handle.getString(mcu.device.iManufacturer, 256))
print("*** Product: %s" % \
        mcu.handle.getString(mcu.device.iProduct, 256))
peri = PeriBoard(mcu)

count = 0
while True:
    try:
        peri.set_led_value(count)
        sw = peri.get_switch()
        light = peri.get_light()

        if sw is True:
            state = "PRESSED"
        else:
            state = "RELEASED"

        print("LEDs set to %d | Switch state: %-8s | Light value: %d" % (
                count, state, light))

        count = (count + 1) % 8
        sleep(0.5)

    except usb.core.USBError:
        print("USB error detected")
