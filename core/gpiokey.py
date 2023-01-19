from datetime import datetime

import RPi.GPIO as GPIO

from core import var

SHORT_PRESS = 15
LONG_PRESS = 150
DELAY_COUNT = 50

KEY_UP = 6
KEY_RIGHT = 26
KEY_DOWN = 19
KEY_LEFT = 5
KEY_PRESS = 13

KEY1 = 21
KEY2 = 20
KEY3 = 16


class Button(object):

    pin = 0
    last_state = 0
    presses = 0

    def __init__(self, pin):
        self.pin = pin

    def update(self):
        if GPIO.input(self.pin):
            self.presses += 1
        else:
            presses = self.presses
            self.presses = 0
            if presses >= SHORT_PRESS:
                if presses >= LONG_PRESS:
                    self.handle(SHORT_PRESS)
                else:
                    self.handle(LONG_PRESS)

    def handle(self, press_type):
        if var.standby:
            var.standby = False
            var.display.command(0x11)
        else:
            var.last_press = self.pin
            var.cur_handle(self.pin, press_type)
        var.last_active = datetime.now()
