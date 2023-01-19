import time
from datetime import datetime

from PIL import Image, ImageDraw

import screens.home
import screens.quit
from core import var, util


message = ""


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    draw.multiline_text((10, 10), text=util.wrap_lines(message, var.font, 220), font=var.font, fill="WHITE")

    return base


def handle(key):
    match key:
        case "KEY1":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
        case "KEY3":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
