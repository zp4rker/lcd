import time
from datetime import datetime

from PIL import Image, ImageDraw

import screens.home
import screens.quit
import screens.splash
from core import var, gpiokey

focus = 0
buttons = [
    "Splash",
    "Button 2",
    "Button 3",
    "Button 4",
    "Quit"
]


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    for i in range(5):
        y1 = 10 + (i * 39.5)
        y2 = 44.5 + (i * 39.5)

        fill = "WHITE" if focus == i else "#353739"
        outline = "BLACK" if focus == i else "WHITE"

        draw.rectangle([10, y1, 230, y2], fill=fill, outline=outline)
        draw.text((120, y1 + 6), text=buttons[i], font=var.font, fill=outline, align="center", anchor="ma")

    return base


def handle(key, press_type):
    global focus
    if press_type == gpiokey.SHORT_PRESS:
        match key:
            case gpiokey.KEY_UP:
                if focus > 0:
                    focus -= 1
                else:
                    focus = 4
            case gpiokey.KEY_DOWN:
                if focus < 4:
                    focus += 1
                else:
                    focus = 0
            case gpiokey.KEY_PRESS:
                if buttons[focus]:
                    _handle_button(buttons[focus])
                    focus = 0
            case gpiokey.KEY3 | gpiokey.KEY1:
                var.cur_screen = screens.home.show
                var.cur_handle = screens.home.handle
                focus = 0


def _handle_button(button):
    match button:
        case "Quit":
            var.cur_screen = screens.quit.show
            var.cur_handle = screens.quit.handle
        case "Splash":
            screens.splash.frame = 0
