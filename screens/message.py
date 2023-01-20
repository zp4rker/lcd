import time
from datetime import datetime

from PIL import Image, ImageDraw

import screens.home
import screens.quit
import screens.youtube
from core import var, util

message = ""
sender = "unknown"

button = None


def show():
    global button
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    text = f"{sender} sent:\n" + message

    if message.startswith("https://youtube.com/watch") or message.startswith("https://youtu.be/"):
        text = f"{sender} sent a YouTube video\n"
        button = "View info"

    draw.multiline_text((10, 10), text=util.wrap_lines(text, var.font, 220), font=var.font, fill="WHITE")

    if button:
        y = 165.5
        draw.rectangle([10, y, 230, 200], fill="WHITE", outline="BLACK")
        draw.text((120, y + 6), text=button, font=var.font, fill="BLACK", align="center", anchor="ma")

    return base


def handle(key):
    match key:
        case "KEY1":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
        case "KEY3":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
        case "KEY_PRESS":
            screens.youtube.url = message
            var.cur_screen = screens.youtube.show
            var.cur_handle = screens.youtube.handle
