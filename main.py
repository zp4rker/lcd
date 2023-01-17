import threading
from datetime import datetime

import spidev as SPI
from PIL import Image, ImageDraw, ImageFont

import ST7789
import listener
import screens.menu
import standby
import var
from util import wrap_lines

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

font = ImageFont.truetype("JetBrainsMono.ttf", size=16)
blink = True
second = datetime.now().second

listener_thread = threading.Thread(target=listener.listen, name="Listener Thread")
listener_thread.start()

standby_thread = threading.Thread(target=standby.watch, name="Standby Thread")
standby_thread.start()

var.cur_screen = screens.menu.show

while not var.quitting:
    base = Image.new("RGB", (disp.width, disp.height), "BLACK")

    if var.standby:
        disp.ShowImage(base, 0, 0)
        continue

    # draw = ImageDraw.Draw(base)
    #
    # date = datetime.now().strftime("%a, %-d %b %y")
    # text = "Today is " + date + "\n"
    # now = datetime.now().strftime("%H:%M" if blink else "%H %M")
    # text += "It is currently " + now + "\n"
    # text += "Press KEY3 to exit\n"
    # if var.last_press:
    #     text += "Last key: " + var.last_press + "\n"
    #
    # draw.multiline_text((0, 0), text=wrap_lines(text, font, disp.width), font=font, fill="WHITE")
    # disp.ShowImage(base, 0, 0)
    #
    # if datetime.now().second != second:
    #     blink = not blink
    #     second = datetime.now().second
    disp.ShowImage(var.cur_screen(), 0, 0)

disp.clear()
