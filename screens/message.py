import time
from datetime import datetime, timedelta

from PIL import Image, ImageDraw
from pytube import YouTube

import screens.home
import screens.quit
from core import var, util


message = ""
sender = "unknown"


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    text = f"{sender} said:\n" + message

    if message.startswith("https://youtube.com/watch"):
        yt = YouTube(message)
        text = f"{sender} sent YouTube video:\n"
        text += f"Title: {yt.title}\n"
        text += f"Length: {timedelta(seconds=yt.length)}\n"
        text += f"Author: {yt.author}\n"

    draw.multiline_text((10, 10), text=util.wrap_lines(text, var.font, 220), font=var.font, fill="WHITE")

    return base


def handle(key):
    match key:
        case "KEY1":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
        case "KEY3":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
