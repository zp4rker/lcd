from PIL import ImageFont

display = None
cur_screen = None
cur_handle = None

font = ImageFont.truetype("JetBrainsMono.ttf", size=17)

last_press = None
quitting = False
standby = False
last_active = None
blink = False
