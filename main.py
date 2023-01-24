from datetime import datetime

import spidev as SPI
from PIL import Image

import screens.home
import screens.splash
from core import ST7789, var, threadhandler

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0
device = 0

disp = ST7789.ST7789(SPI.SpiDev(bus, device), RST, DC, BL)
disp.Init()
disp.clear()
var.display = disp

second = datetime.now().second

var.cur_screen = screens.home.show
var.cur_handle = screens.home.handle

while not var.quitting:
    if screens.splash.frame < 55:
        disp.ShowImage(screens.splash.show(), 0, 0)
        continue

    threadhandler.start_threads()

    if var.standby:
        continue

    if datetime.now().second != second:
        var.blink = not var.blink
        second = datetime.now().second

    disp.ShowImage(var.cur_screen(), 0, 0)

disp.clear()
disp.ShowImage(Image.new("RGB", (disp.width, disp.height), "BLACK"), 0, 0)
