import datetime

from PIL import Image

import screens.home
from core import var

last_frame = datetime.datetime.now()
frame = 0

im = Image.open("assets/splash.gif")


def show():
    global last_frame, frame
    base = Image.new("RGB", (240, 240), "#353739")

    try:
        # if (datetime.datetime.now() - last_frame).microseconds >= 100:
        #     print(f"frame {frame} - {(datetime.datetime.now() - last_frame).microseconds}ms")
        #     frame += 1
        #     last_frame = datetime.datetime.now()
        im.seek(frame)
        base.paste(im, (0, 0))
        frame += 1
    except EOFError:
        var.cur_screen = screens.home.show
        var.cur_handle = screens.home.handle

    return base


def handle(key, press_type):
    pass
