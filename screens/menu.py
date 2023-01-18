from PIL import Image, ImageDraw


def show():
    base = Image.new("RGB", (240, 240), "BLACK")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)

    return base
