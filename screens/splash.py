import time

from PIL import Image

import screens.home
from core import var


def show():
    base = Image.new("RGB", (240, 240), "#353739")

    with Image.open("assets/splash.gif") as im:
        im.seek(0)
        time.sleep(0.1)
        try:
            while True:
                im.seek(im.tell() + 1)
                base.paste(im, (0, 0))
                time.sleep(0.1)
        except EOFError:
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle

    return base


def handle(key, press_type):
    pass
