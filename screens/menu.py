from PIL import Image, ImageDraw

import var

focus = -1


def show():
    base = Image.new("RGB", (240, 240), "BLACK")
    draw = ImageDraw.Draw(base)

    draw.line([(0, 210), (240, 210)], fill="WHITE", width=1)

    for i in range(5):
        y1 = 20 + (i * 35)
        y2 = 50 + (i * 35)

        fill = "WHITE" if focus == i else "BLACK"
        outline = "BLACK" if focus == i else "WHITE"

        draw.rectangle([20, y1, 220, y2], fill=fill, outline=outline)
        draw.text((25, y1 + 5), text=f"Button {i}", font=var.font, fill=outline)

    # draw.rectangle([(20, 20), (220, 50)], fill="BLACK", outline="WHITE")
    # draw.text((25, 25), text="Button 1", font=var.font, fill="WHITE")
    #
    # draw.rectangle([(20, 55), (220, 85)], fill="BLACK", outline="WHITE")
    # draw.text((25, 60), text="Button 2", font=var.font, fill="WHITE")
    #
    # draw.rectangle([(20, 90), (220, 120)], fill="BLACK", outline="WHITE")
    # draw.text((25, 95), text="Button 3", font=var.font, fill="WHITE")
    #
    # draw.rectangle([(20, 125), (220, 155)], fill="BLACK", outline="WHITE")
    # draw.text((25, 130), text="Button 4", font=var.font, fill="WHITE")
    #
    # draw.rectangle([(20, 160), (220, 190)], fill="BLACK", outline="WHITE")
    # draw.text((25, 165), text="Button 5", font=var.font, fill="WHITE")

    return base


def handle(key):
    global focus
    match key:
        case "KEY_UP":
            if focus > 0:
                focus -= 1
        case "KEY_DOWN":
            if focus < 4:
                focus += 1
