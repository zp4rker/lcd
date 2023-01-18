import time
from datetime import datetime

from PIL import Image, ImageDraw

import screens.menu
import var


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y | " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((5, 215), text=timestr, font=var.font, fill="WHITE")

    return base


def handle(key):
    match key:
        case "KEY3":
            var.cur_screen = screens.menu.show
            var.cur_handle = screens.menu.handle
