import time

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
        if not GPIO.input(KEY_UP_PIN):
            print("KEY_UP")
            var.last_press = "KEY_UP"
            time.sleep(0.3)

        if not GPIO.input(KEY_RIGHT_PIN):
            print("KEY_RIGHT")
            var.last_press = "KEY_RIGHT"
            time.sleep(0.3)

        if not GPIO.input(KEY_DOWN_PIN):
            print("KEY_DOWN")
            var.last_press = "KEY_DOWN"
            time.sleep(0.3)

        if not GPIO.input(KEY_LEFT_PIN):
            print("KEY_LEFT")
            var.last_press = "KEY_LEFT"
            time.sleep(0.3)

        if not GPIO.input(KEY_PRESS_PIN):
            print("KEY_PRESS")
            var.last_press = "KEY_PRESS"
            time.sleep(0.3)

        if not GPIO.input(KEY1_PIN):
            print("KEY1")
            var.last_press = "KEY1"
            time.sleep(0.3)

        if not GPIO.input(KEY2_PIN):
            print("KEY2")
            var.last_press = "KEY2"
            time.sleep(0.3)

        if not GPIO.input(KEY3_PIN):
            print("KEY3")
            var.last_press = "KEY3"
            time.sleep(0.3)
            var.quit = True
            quit()
