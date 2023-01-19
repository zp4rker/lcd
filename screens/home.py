import socket
import time
from datetime import datetime, timedelta

import psutil
from PIL import Image, ImageDraw
from gpiozero import CPUTemperature

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
    text = f"Hostname: {socket.gethostname()}\n"
    ip = ""
    for addr in psutil.net_if_addrs()["wlan0"]:
        if addr.netmask.startswith("255"):
            ip = addr.address
            break
    text += f"IP: {ip}\n"
    text += f"Uptime: {_uptime()}"
    cpu = CPUTemperature()
    text += f"CPU: {psutil.cpu_percent()}% ({round(cpu.temperature, 1)}C)\n"
    text += f"Memory: {psutil.virtual_memory().percent}%\n"
    text += f"Storage: {psutil.disk_usage('/').percent}%\n"

    draw.multiline_text((10, 10), text=util.wrap_lines(text, var.font, 220), font=var.font, fill="WHITE")

    return base


def handle(key):
    match key:
        case "KEY3":
            var.cur_screen = screens.menu.show
            var.cur_handle = screens.menu.handle


def _uptime():
    raw = psutil.boot_time()
    td = timedelta(seconds=raw)
    comps = str(td).split(":")
    return f"{comps[0]} hours, {comps[1]} minutes, {comps[2]} seconds"
