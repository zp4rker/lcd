import time

import RPi.GPIO as GPIO

from core import var, gpiokey


gpiokeys = [
    gpiokey.Button(gpiokey.KEY_UP),
    gpiokey.Button(gpiokey.KEY_RIGHT),
    gpiokey.Button(gpiokey.KEY_DOWN),
    gpiokey.Button(gpiokey.KEY_LEFT),
    gpiokey.Button(gpiokey.KEY_PRESS),

    gpiokey.Button(gpiokey.KEY1),
    gpiokey.Button(gpiokey.KEY2),
    gpiokey.Button(gpiokey.KEY3)
]


def listen():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpiokey.KEY_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY_PRESS, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(gpiokey.KEY3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while not var.quitting:
        for b in gpiokeys:
            b.update()
        time.sleep(0.01)
