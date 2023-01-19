import os
import time
from datetime import datetime

import git
from PIL import Image, ImageDraw

import screens.home
import screens.quit
from core import var

focus = 0
buttons = [
    "Restart app",
    "Update app",
    "Reboot",
]


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    for i in range(3):
        y1 = 10 + (i * 39.5)
        y2 = 44.5 + (i * 39.5)

        fill = "WHITE" if focus == i else "#353739"
        outline = "BLACK" if focus == i else "WHITE"

        draw.rectangle([10, y1, 230, y2], fill=fill, outline=outline)
        draw.text((120, y1 + 6), text=buttons[i], font=var.font, fill=outline, align="center", anchor="ma")

    return base


def handle(key):
    global focus
    match key:
        case "KEY_UP":
            if focus > 0:
                focus -= 1
        case "KEY_DOWN":
            if focus < 4:
                focus += 1
        case "KEY_PRESS":
            if buttons[focus]:
                _handle_button(buttons[focus])
                focus = 0
        case "KEY1":
            var.cur_screen = screens.quit.show
            var.cur_handle = screens.quit.handle
            focus = 0
        case "KEY3":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
            focus = 0


def _handle_button(button):
    match button:
        case "Restart app":
            var.quitting = True
            os.system("python3 main.py &")
        case "Update app":
            var.quitting = True
            repo = git.Repo("./")
            repo.remotes.origin.pull()
            os.system("python3 main.py &")
        case "Reboot":
            var.quitting = True
            os.system("reboot")
