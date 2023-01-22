def wrap_lines(string, font, width):
    output = ""

    for line in string.split("\n"):
        cur = ""
        beg = 0

        for i in range(len(line)):
            if line[i] == " " and i < len(line):
                if i > beg:
                    s = line[beg:i + 1]
                    # print("s=", s)
                    if font.getlength(cur + s) < width:
                        cur += s
                    else:
                        output += cur + "\n"
                        # print("cur=", cur)
                        # print("length=", font.getlength(cur))
                        # print("potlength=", font.getlength(cur + s))
                        cur = s
                beg = i + 1
        if beg + 1 < len(line):
            s = line[beg:]
            if font.getlength(cur + s) < width:
                output += cur + s
            else:
                output += cur + "\n"
                output += s
        output += "\n"
    return output
