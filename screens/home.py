import socket
import time
from datetime import datetime, timedelta

import psutil
from PIL import Image, ImageDraw
from gpiozero import CPUTemperature

import screens.menu
from core import util, var, gpiokey


def show():
    base = Image.new("RGB", (240, 240), "#353739")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)
    timestr = time.strftime("%a %-d %b %Y " + ("%H:%M" if var.blink else "%H %M")).format(datetime.now())
    draw.text((120, 215), text=timestr, font=var.font, fill="WHITE", align="center", anchor="ma")

    # stats
    text = f"Hostname: {socket.gethostname()}\n"
    ip = ""
    for addr in psutil.net_if_addrs()["wlan0"]:
        if addr.netmask.startswith("255"):
            ip = addr.address
            break
    text += f"IP: {ip}\n"
    text += f"Uptime: {_uptime()}\n"
    cpu = CPUTemperature()
    text += f"CPU: {psutil.cpu_percent()}% ({round(cpu.temperature, 1)}C)\n"
    text += f"Memory: {psutil.virtual_memory().percent}%\n"
    text += f"Storage: {psutil.disk_usage('/').percent}%\n"

    draw.multiline_text((10, 10), text=util.wrap_lines(text, var.font, 220), font=var.font, fill="WHITE")

    return base


def handle(key, press_type):
    if press_type == gpiokey.SHORT_PRESS:
        match key:
            case gpiokey.KEY3:
                var.cur_screen = screens.menu.show
                var.cur_handle = screens.menu.handle
            case gpiokey.KEY1:
                var.standby = True
                var.display.command(0x28)


def _uptime():
    raw = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    td = timedelta(seconds=raw.seconds)
    comps = str(td).split(":")
    return f"{comps[0]}h, {comps[1]}m"
