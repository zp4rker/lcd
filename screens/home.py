import socket
import time
from datetime import datetime

import psutil
from PIL import Image, ImageDraw

import screens.menu
import util
import var


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y | " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((5, 215), text=timestr, font=var.font, fill="WHITE")

    # stats
    text = f"Hostname: {socket.gethostname()}"
    ip = ""
    for addr in psutil.net_if_addrs()["wlan0"]:
        if addr.netmask.startswith("255"):
            ip = addr.address
            break
    text += f"IP: {ip}\n"

    draw.multiline_text((10, 10), text=util.wrap_lines(text, var.font, 220), font=var.font, fill="WHITE")

    return base


def handle(key):
    match key:
        case "KEY3":
            var.cur_screen = screens.menu.show
            var.cur_handle = screens.menu.handle
