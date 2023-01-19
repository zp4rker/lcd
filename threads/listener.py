import time
from datetime import datetime

import RPi.GPIO as GPIO

from core import var

KEY_UP_PIN = 6
KEY_DOWN_PIN = 19
KEY_LEFT_PIN = 5
KEY_RIGHT_PIN = 26
KEY_PRESS_PIN = 13

KEY1_PIN = 21
KEY2_PIN = 20
KEY3_PIN = 16


def listen():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(KEY_UP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_RIGHT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_DOWN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_LEFT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY_PRESS_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(KEY3_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while not var.quitting:
        key = None
        if not GPIO.input(KEY_UP_PIN):
            key = "KEY_UP"

        if not GPIO.input(KEY_RIGHT_PIN):
            key = "KEY_RIGHT"

        if not GPIO.input(KEY_DOWN_PIN):
            key = "KEY_DOWN"

        if not GPIO.input(KEY_LEFT_PIN):
            key = "KEY_LEFT"

        if not GPIO.input(KEY_PRESS_PIN):
            key = "KEY_PRESS"

        if not GPIO.input(KEY1_PIN):
            key = "KEY1"

        if not GPIO.input(KEY2_PIN):
            key = "KEY2"

        if not GPIO.input(KEY3_PIN):
            key = "KEY3"

        if key:
            if var.standby:
                var.standby = False
            else:
                var.last_press = key
                var.cur_handle(key)
            var.last_active = datetime.now()
            time.sleep(0.3)
