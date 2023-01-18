import threading
from datetime import datetime

import spidev as SPI
from PIL import Image

import ST7789
import listener
import screens.menu
import standby
import var

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

listener_thread = threading.Thread(target=listener.listen, name="Listener Thread")
listener_thread.start()

standby_thread = threading.Thread(target=standby.watch, name="Standby Thread")
standby_thread.start()

var.cur_screen = screens.menu.show
var.cur_handle = screens.menu.handle

while not var.quitting:
    base = Image.new("RGB", (disp.width, disp.height), "BLACK")

    if var.standby:
        disp.ShowImage(base, 0, 0)
        continue

    if datetime.now().second != second:
        var.blink = not var.blink
        second = datetime.now().second

    disp.ShowImage(var.cur_screen(), 0, 0)

disp.clear()
disp.ShowImage(Image.new("RGB", (disp.width, disp.height), "BLACK"), 0, 0)
