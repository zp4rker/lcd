import asyncio

import spidev as SPI
import ST7789
import time

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

import listener
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

font = ImageFont.truetype("JetBrainsMono.ttf", size=16)
blink = True

await listener.listen()

while True:
    base = Image.new("RGB", (disp.width, disp.height), "BLACK")
    draw = ImageDraw.Draw(base)

    date = datetime.now().strftime("%a, %-d %b %y")
    text = "Today is " + date + "\n"
    now = datetime.now().strftime("%H:%M" if blink else "%H %M")
    text += "It is currently " + now + "\n"
    draw.multiline_text((0, 0), text=wrap_lines(text, font, disp.width), font=font, fill="WHITE")
    disp.ShowImage(base, 0, 0)
    blink = not blink
    time.sleep(1)
