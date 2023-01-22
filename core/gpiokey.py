from datetime import datetime

import RPi.GPIO as GPIO

from core import var

KEY_UP = 6
KEY_DOWN = 19
KEY_LEFT = 5
KEY_RIGHT = 26
KEY_PRESS = 13

KEY1 = 21
KEY2 = 20
KEY3 = 16

SHORT_PRESS = 100
LONG_PRESS = 101


class Key(object):
    pin = 0
    presses = 0

    def __init__(self, pin):
        self.pin = pin

    def update(self):
        if GPIO.input(self.pin):
            if self.presses > 0:
                if var.standby:
                    var.standby = False
                    var.display.command(0x11)
                elif self.presses > SHORT_PRESS:
                    var.cur_handle(self.pin, LONG_PRESS)
                else:
                    var.cur_handle(self.pin, SHORT_PRESS)
                self.presses = 0
                var.last_active = datetime.now()
            else:
                self.presses += 1
