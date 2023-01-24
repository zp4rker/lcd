from PIL import Image

import screens.home
from core import var

frame = 0

im = Image.open("assets/splash.gif")


def show():
    global frame
    base = Image.new("RGB", (240, 240), "#353739")

    try:
        im.seek(frame)
        base.paste(im, (0, 0))
        frame += 1
    except EOFError:
        var.cur_screen = screens.home.show
        var.cur_handle = screens.home.handle

    return base


def handle(key, press_type):
    pass
