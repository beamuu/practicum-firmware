import usb

RQ_SET_LED       = 0
RQ_SET_LED_VALUE = 1
RQ_GET_SWITCH    = 2
RQ_GET_LIGHT     = 3
RQ_GET_REED      = 4

####################################
def find_mcu_boards():
    '''
    Find all Practicum MCU boards attached to the machine, then return a list
    of USB device handles for all the boards

    >>> devices = find_mcu_boards()
    >>> first_board = McuBoard(devices[0])
    '''
    boards = [dev for bus in usb.busses()
                  for dev in bus.devices
                  if (dev.idVendor,dev.idProduct) == (0x16c0,0x05dc)]
    return boards

####################################
class McuBoard:
    '''
    Generic class for accessing Practicum MCU board via USB connection.
    '''

    ################################
    def __init__(self, dev):
        self.device = dev
        self.handle = dev.open()

    ################################
    def usb_write(self, request, data=[], index=0, value=0):
        '''
        Send data output to the USB device (i.e., MCU board)
           request: request number to appear as bRequest field on the USB device
           index: 16-bit value to appear as wIndex field on the USB device
           value: 16-bit value to appear as wValue field on the USB device
        '''
        reqType = usb.TYPE_VENDOR | usb.RECIP_DEVICE | usb.ENDPOINT_OUT
        self.handle.controlMsg(
                reqType, request, data, value=value, index=index)

    ################################
    def usb_read(self, request, length=1, index=0, value=0):
        '''
        Request data input from the USB device (i.e., MCU board)
           request: request number to appear as bRequest field on the USB device
           length: number of bytes to read from the USB device
           index: 16-bit value to appear as wIndex field on the USB device
           value: 16-bit value to appear as wValue field on the USB device

        If successful, the method returns a tuple of length specified
        containing data returned from the MCU board.
        '''
        reqType = usb.TYPE_VENDOR | usb.RECIP_DEVICE | usb.ENDPOINT_IN
        buf = self.handle.controlMsg(
                reqType, request, length, value=value, index=index)
        return buf


####################################
class PeriBoard:

    ################################
    def __init__(self, mcu):
        self.mcu = mcu

    ################################
    def set_led(self, led_no, led_state):
        '''
        Set status of LED led_no on peripheral board to led_state
        (0 => off, 1 => on)
        '''
        self.mcu.usb_write(RQ_SET_LED, index=led_no, value=led_state)

    ################################
    def set_led_value(self, value):
        '''
        Display right 3 bits of value on peripheral board's LEDs
        '''
        self.mcu.usb_write(RQ_SET_LED_VALUE, value=value)

    ################################
    def get_switch(self):
        '''
        Return a boolean value indicating whether the switch on the peripheral
        board is currently pressed
        '''
        state = self.mcu.usb_read(RQ_GET_SWITCH, length=1)[0]
        return (state != 0)

    ################################
    def get_light(self):
        '''
        Return the current reading of light sensor on peripheral board
        '''
        low,high = self.mcu.usb_read(RQ_GET_LIGHT, 2)
        return low+high*256
    def getReedId(self):
        state = self.mcu.usb_read(request=REQ_GET_REED,length=1)
        return state[0]
