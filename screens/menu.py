from PIL import Image, ImageDraw


def show():
    base = Image.open("screens/images/menu.png")
    button = Image.open("screens/images/button-highlighted.png")
    base.paste(button, (20, 20))
    return base
