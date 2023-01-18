import spidev as SPI
from PIL import Image

import ST7789

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0
device = 0

disp = ST7789.ST7789(SPI.SpiDev(bus, device), RST, DC, BL)
disp.Init()
disp.clear()

base = Image.new("RGB", (disp.width, disp.height), "BLACK")
disp.ShowImage(base, 0, 0)
