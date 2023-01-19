import time
from datetime import datetime

from PIL import Image, ImageDraw

import screens.home
import screens.menu
import screens.reboot
import screens.shutdown
import var

focus = 0
buttons = [
    "Quit",
    "Restart",
]


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y | " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    for i in range(2):
        y1 = 20 + (i * 35)
        y2 = 50 + (i * 35)

        fill = "WHITE" if focus == i else "#353739"
        outline = "BLACK" if focus == i else "WHITE"

        draw.rectangle([20, y1, 220, y2], fill=fill, outline=outline)
        draw.text((120, y1 + 5), text=buttons[i], font=var.font, fill=outline, align="center", anchor="ma")

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
            var.cur_screen = screens.menu.show
            var.cur_handle = screens.menu.handle
            focus = 0
        case "KEY3":
            var.cur_screen = screens.home.show
            var.cur_handle = screens.home.handle
            focus = 0


def _handle_button(button):
    match button:
        case "Quit":
            var.cur_screen = screens.shutdown.show
            var.cur_handle = screens.shutdown.handle
        case "Restart":
            var.cur_screen = screens.reboot.show
            var.cur_handle = screens.reboot.handle
