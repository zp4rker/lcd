import os
import time
from datetime import datetime

from PIL import Image, ImageDraw

import screens.quit
import var

focus = 0
buttons = [
    "Restart application",
    "Update application",
    "Reboot machine",
]


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y | " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((5, 215), text=timestr, font=var.font, fill="WHITE")

    for i in range(3):
        y1 = 20 + (i * 35)
        y2 = 50 + (i * 35)

        fill = "WHITE" if focus == i else "#353739"
        outline = "BLACK" if focus == i else "WHITE"

        draw.rectangle([20, y1, 220, y2], fill=fill, outline=outline)
        draw.text((25, y1 + 5), text=buttons[i], font=var.font, fill=outline)

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
        case "KEY3":
            var.cur_screen = screens.quit.show
            var.cur_handle = screens.quit.handle
            focus = 0


def _handle_button(button):
    match button:
        case "Restart application":
            var.quitting = True
            os.system("python3 main.py &")
        case "Update application":
            var.quitting = True
            os.system('runuser -l zp4rker -c "cd /home/zp4rker/lcd && git reset --hard && git pull" && python3 main.py')
        case "Reboot machine":
            var.quitting = True
            os.system("reboot")
