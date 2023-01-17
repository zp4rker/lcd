import time
from datetime import datetime

import RPi.GPIO as GPIO

import var

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

    while True:
        press = False
        if not GPIO.input(KEY_UP_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY_UP")
                var.last_press = "KEY_UP"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY_RIGHT_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY_RIGHT")
                var.last_press = "KEY_RIGHT"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY_DOWN_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY_DOWN")
                var.last_press = "KEY_DOWN"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY_LEFT_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY_LEFT")
                var.last_press = "KEY_LEFT"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY_PRESS_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY_PRESS")
                var.last_press = "KEY_PRESS"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY1_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY1")
                var.last_press = "KEY1"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY2_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY2")
                var.last_press = "KEY2"
                var.last_active = datetime.now()
            press = True

        if not GPIO.input(KEY3_PIN):
            if var.standby:
                var.standby = False
                var.last_active = datetime.now()
            else:
                print("KEY3")
                var.last_press = "KEY3"
                var.last_active = datetime.now()
                var.quitting = True
                quit()
            press = True

        if press:
            time.sleep(0.3)
