import RPi.GPIO as GPIO

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
        if GPIO.input(KEY_UP_PIN):
            # released
            print("KEY_UP - Released")
        else:
            # pressed
            print("KEY_UP - Pressed")
        if GPIO.input(KEY_RIGHT_PIN):
            # released
            print("KEY_RIGHT - Released")
        else:
            # pressed
            print("KEY_RIGHT - Pressed")
        if GPIO.input(KEY_DOWN_PIN):
            # released
            print("KEY_DOWN - Released")
        else:
            # pressed
            print("KEY_DOWN - Pressed")
        if GPIO.input(KEY_LEFT_PIN):
            # released
            print("KEY_LEFT - Released")
        else:
            # pressed
            print("KEY_LEFT - Pressed")
        if GPIO.input(KEY_PRESS_PIN):
            # released
            print("KEY_PRESS - Released")
        else:
            # pressed
            print("KEY_PRESS - Pressed")
        if GPIO.input(KEY1_PIN):
            # released
            print("KEY1 - Released")
        else:
            # pressed
            print("KEY1 - Pressed")
        if GPIO.input(KEY2_PIN):
            # released
            print("KEY2 - Released")
        else:
            # pressed
            print("KEY2 - Pressed")
        if GPIO.input(KEY3_PIN):
            # released
            print("KEY3 - Released")
        else:
            # pressed
            print("KEY3 - Pressed")
