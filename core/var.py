from datetime import datetime

from PIL import ImageFont

display = None
cur_screen = None
cur_handle = None

font = ImageFont.truetype("JetBrainsMono.ttf", size=17)

quitting = False
standby = False
last_active = datetime.now()
blink = False
