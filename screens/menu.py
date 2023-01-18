import time
from datetime import datetime

from PIL import Image, ImageDraw

import var

focus = -1


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)

    for i in range(5):
        y1 = 20 + (i * 35)
        y2 = 50 + (i * 35)

        fill = "WHITE" if focus == i else "#353739"
        outline = "BLACK" if focus == i else "WHITE"

        draw.rectangle([20, y1, 220, y2], fill=fill, outline=outline)
        draw.text((25, y1 + 5), text=f"Button {i}", font=var.font, fill=outline)

    draw.text((5, 215), text=time.strftime("%H:%M:%S").format(datetime.now()), font=var.font, fill="WHITE")

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
