import threading
import time

import RPi.GPIO as GPIO

from core import var, gpiokey

keys = [
    gpiokey.Key(gpiokey.KEY_UP),
    gpiokey.Key(gpiokey.KEY_RIGHT),
    gpiokey.Key(gpiokey.KEY_DOWN),
    gpiokey.Key(gpiokey.KEY_LEFT),
    gpiokey.Key(gpiokey.KEY_PRESS),
    gpiokey.Key(gpiokey.KEY1),
    gpiokey.Key(gpiokey.KEY2),
    gpiokey.Key(gpiokey.KEY3),
]


class Listener(threading.Thread):
    def run(self) -> None:
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
            for key in keys:
                key.update()
            time.sleep(0.01)
